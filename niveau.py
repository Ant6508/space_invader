"""
Codé par : RONGERE Julien et Rodde Théophile

    Ce fichier contient la classe niveau qui permet de créer un niveau

    A faire : -ajouter la musique
    """

from pygame import mixer
import time
import bonus
import random 
import menu
import funaux
class niveau:

    def __init__(self,master,canvas,fenetre,score_multiplieur) -> None:
        
        self.master = master
        self.fenetre = fenetre
        self.canvas = canvas
        self.score_multiplieur = score_multiplieur

        mixer.init() # on initialise le mixer de pygame
        mixer.music.load("musiques/niveaux/"+ str(self.master.niveau_courant) +".mp3"  ) # on charge la musique qui correspond au niveau
        self.fenetre.after(0,mixer.music.play) #on la joue

        self.vague_courante = 0 # on initialise la vague courante à 0
        self.etat = "en cours" # on initialise l'état du niveau à verrouille parmis : verrouille, en cours, fini

        self.fenetre.bind("c",lambda event: self.master.menu.entrer_code()) # on lie la touche c à la fonction qui permet d'entrer un code

        self.empecher_spawn = False # on initialise la variable qui permet d'empêcher le spawn des aliens à False

        self.vitesse_aliens() # on lance la fonction qui augmente la vitesse des aliens
        self.fenetre.after(0,self.spawn_protection) # on lance la fonction qui fait spawn les protections

        self.protections = []

        self.fonctions_deplacement = {"sbire":[],"shooter":[],"boss2":[],"boss3":[]} # dictionnaire qui contient les fonctions de déplacement des aliens en fonction de leur type
        #on omet le boss1 et le soldat car ils ont des déplacements spécifiques implémentés dans la classe alien
        self.fenetre.after(0,self.init_deplacements) # on initialise les fonctions de déplacement des aliens
        

    def init_deplacements(self):
        #fonction qui initialise les fonctions de déplacement des aliens en fonction de leur type et de la vague courante

        
        for type_alien in self.fonctions_deplacement.keys(): # on parcourt les types d'aliens

            #si le type d'alien n'est pas dans la liste des aliens de la vague courante on passe au type d'alien suivant
            if type_alien not in [alien.__class__.__name__ for alien in self.aliens_waves[self.vague_courante]]:
                continue

            for vague in range(len(self.aliens_waves)+1): # on parcourt les vagues
                fonction = getattr(self,"deplacement_"+type_alien.lower() + "_" + str(vague),None) # on récupère la fonction de déplacement de l'alien

                if fonction != None: # si la fonction existe
                    self.fonctions_deplacement[type_alien].append(fonction) # on l'ajoute à la liste des fonctions de déplacement de l'alien
                else : # sinon
                    self.fonctions_deplacement[type_alien].append( self.fonctions_deplacement[type_alien][0]) # on ajoute la fonction de déplacement de la première vague
                
    def spawn_aliens(self,wave=0):
        # fonction qui fait spawn les aliens

        if self.empecher_spawn == True: # si la variable qui empêche le spawn est à True on ne fait rien
            return
        for i in range(len(self.aliens_waves[wave])): # on parcourt la liste des aliens de la vague
            alien =  self.aliens_waves[wave][i]
            self.fenetre.after(500*i,self.master.aliens.append,self.aliens_waves[wave][i])   # on ajoute l'alien à la liste des aliens du master
            type_alien = alien.__class__.__name__ # on récupère le type de l'alien en regardant le nom de sa classe

            self.fenetre.after(500*i,alien.spawn) # on fait spawn l'alien            
            self.fenetre.after(500*i,self.change_a_spawn,alien) # on change la variable qui permet de savoir si l'alien a spawn ou non

            if type_alien != "boss1" and type_alien != "soldat": 
                fonction_deplacement = self.fonctions_deplacement[type_alien][wave] # on récupère la fonction de déplacement de l'alien en fonction de sa vague
                self.fenetre.after(500*i,fonction_deplacement,alien) # on lance la fonction de déplacement de l'alien


        self.fenetre.after(1000,self.prochaine_vague,self.vague_courante) # on lance la fonction qui vérifie si la vague est finie
        self.spawn_bonus()
        self.vitesse_aliens()

    def change_a_spawn(self,alien):
        #fonction qui change la variable qui permet de savoir si l'alien a spawn ou non

        alien.a_spawn = not alien.a_spawn

    def prochaine_vague(self,vague_courante=0):
        #fonction qui vérifie si la vague est finie et si oui lance la vague suivante ou la fin du niveau
        if self.etat == "fini" or self.etat == "verrouille":
            return

        if not all([alien.etat == "mort" for alien in self.aliens_waves[vague_courante]]): # si tous les aliens de la vague courante ne sont pas morts
            self.fenetre.after(1000,self.prochaine_vague,vague_courante) # on attend 1 seconde et on relance la fonction

        elif self.vague_courante == len(self.aliens_waves)-1: # si c'est la dernière vague
            self.fenetre.after(0,self.fin_niveau,True) # on lance la fonction de fin de niveau avec comme argument True (victoire)

        else:
            self.master.aliens = []
            self.vague_courante += 1
            self.fenetre.after(5000,self.spawn_aliens,vague_courante+1) # sinon on fait spawn la vague suivante

    def fin_niveau(self,bool_victoire):
        # fonction qui s'execute à la fin du niveau (victoire ou défaite) faisant le menage et rendant les boutons des niveaux précédents cliquables

        self.fenetre.after(0,mixer.music.stop) # on arrête la musique

        self.master.nettoyage_complet()

        for bouton in self.master.boutton_niveaux_liste[:self.master.der_niveau]: # on rend les boutons des niveaux précédents cliquables
            bouton.config(state="normal")
        
        if bool_victoire: # si le joueur a gagné

            if self.master.niveau_courant == self.master.der_niveau:

                self.master.boutton_niveaux_liste[self.master.der_niveau].config(state="normal")
                self.master.der_niveau += 1             

                
            self.etat = "fini"
            self.master.score.set(self.master.score.get()+1000) # on ajoute 1000 points au score
        else:
            
            self.etat = "verrouille"
         

        self.master.menu.init_menu_accueil() # on lance le menu d'accueil

    def spawn_bonus(self):
        # fonction qui fait spawn un bonus aléatoirement


        if self.etat != "en cours":
            return

        # on fait spawn un bonus aléatoirement
        chance_spawn = 0.1 # chance de faire spawn un bonus
        if random.random() < chance_spawn:
            bonus_type = random.choice(["vie", "tir", "vitesse"]) # on choisit le type de bonus aléatoirement
            position_initiale = [random.randint(0,self.canvas.winfo_width()),random.randint(0,self.canvas.winfo_height())]#on choisit une position initiale aléatoire sur le canvas
            self.master.bonus.append(bonus.bonus(self.master,self.canvas,self.fenetre,position_initiale,bonus_type))
            self.master.bonus[-1].spawn()
        self.fenetre.after(10000,self.spawn_bonus)

    def vitesse_aliens(self):
        #fonction qui augmente la vitesse des aliens lorsqu'ils sont peu nombreux

        if len(self.master.aliens) < 5:
            for alien in self.master.aliens:
                alien.vitesse += 10

        else :
            self.fenetre.after(1000,self.vitesse_aliens)

    def spawn_protection(self):

        #fonction qui fait spawn une protection

        if self.etat != "en cours":
            return

        for protection in self.protections:
            protection.spawn()