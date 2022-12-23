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
        #self.fenetre.after(0,mixer.music.play) #on la joue

    def spawn_aliens(self,wave=0): # fonction qui fait spawn les aliens
        
        for i in range(len(self.aliens_waves[wave])):
            
            type_alien = self.aliens_waves[wave][i].__class__.__name__
            fonction_deplacement = eval("self.deplacement_"+type_alien.lower())
            self.fenetre.after(0,self.aliens_waves[wave][i].spawn)
            self.fenetre.after(0,fonction_deplacement,self.aliens_waves[wave][i])

            if self.prochaine_vague() and wave < len(self.aliens_waves)-1:
                print("prochaine vague dans 5 secondes")
                self.fenetre.after(5,self.spawn_aliens,wave+1)
    
    def prochaine_vague(self,vague_courante=0):
        if not all([alien.etat == "mort" for alien in self.aliens_waves[vague_courante]]):
            return self.fenetre.after(1000,self.prochaine_vague)
        
        else:
            return True