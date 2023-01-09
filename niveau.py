"""
Codé par : RONGERE Julien et Rodde Théophile

    Ce fichier contient la classe niveau qui permet de créer un niveau

    A faire : -ajouter la musique
    """

from pygame import mixer
import time
class niveau:

    def __init__(self,master,canvas,fenetre,score_multiplieur,musique) -> None:
        
        self.master = master
        self.fenetre = fenetre
        self.canvas = canvas
        self.score_multiplieur = score_multiplieur
        self.musique = musique

        mixer.init() # on initialise le mixer de pygame
        mixer.music.load(self.musique) # on charge la musique
        self.fenetre.after(0,mixer.music.play) #on la joue

    def spawn_aliens(self,wave=0): # fonction qui fait spawn les aliens
        
        for i in range(len(self.aliens_waves[wave])):
            self.fenetre.after(500*i,self.master.aliens.append,self.aliens_waves[wave][i])   # on ajoute l'alien à la liste des aliens du master
            type_alien = self.aliens_waves[wave][i].__class__.__name__ # on récupère le type de l'alien en regardant le nom de sa classe
            fonction_deplacement = eval("self.deplacement_"+type_alien.lower()) # on récupère la fonction de déplacement de l'alien en fonction de son type

            self.fenetre.after(500*i,self.aliens_waves[wave][i].spawn)
            self.fenetre.after(500*i,fonction_deplacement,self.aliens_waves[wave][i])

        print([alien.etat for alien in self.aliens_waves[wave]])

        if wave < len(self.aliens_waves)-1: # si ce n'est pas la dernière vague
            self.fenetre.after(0,self.prochaine_vague,wave)

    def prochaine_vague(self,vague_courante=0):

        if not all([alien.etat == "mort" for alien in self.aliens_waves[vague_courante]]): # si tous les aliens de la vague courante ne sont pas morts
            self.fenetre.after(1000,self.prochaine_vague,vague_courante) # on attend 1 seconde et on relance la fonction
        else:
            print("vague suivante dans 5 secondes")
            self.fenetre.after(5000,self.spawn_aliens,vague_courante+1) # sinon on fait spawn la vague suivante