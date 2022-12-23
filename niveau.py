"""
Codé par : RONGERE Julien et Rodde Théophile

    Ce fichier contient la classe niveau qui permet de créer un niveau

    A faire : -ajouter la musique
    """

from pygame import mixer

class niveau:

    def __init__(self,master,canvas,fenetre,score_multiplieur,musique) -> None:
        
        self.master = master
        self.fenetre = fenetre
        self.canvas = canvas
        self.score_multiplieur = score_multiplieur
        self.musique = musique

        mixer.init() # on initialise le mixer de pygame
        mixer.music.load(self.musique) # on charge la musique
        #self.fenetre.after(0,mixer.music.play) #on la joue

    def spawn_aliens(self): # fonction qui fait spawn les aliens
        
        for wave in self.aliens_waves:
            for i in range(len(wave)):
                fonction_deplacement = getattr(self,"deplacement_"+wave[i].__class__.__name__.lower()) # on récupère la fonction de déplacement de l'alien
                self.fenetre.after(1000*i,wave[i].spawn) # on fait spawn les aliens avec un délai de 1 seconde entre chaque alien
                self.fenetre.after(1000*i,fonction_deplacement,wave[i]) # on fait déplacer les aliens avec un délai de 1 seconde entre chaque alien
                self.fenetre.after(1000*i,self.master.aliens.append,wave[i]) # on ajoute les aliens à la liste des aliens du master avec un délai de 1 seconde entre chaque alien