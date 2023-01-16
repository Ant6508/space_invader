'''
Codé par : RONGERE Julien et Rodde Théophile
Date : 05/12/202
Version : 1.0
Description : Class des aliens desquelles vont découlés les autres aliens
'''
import tkinter as tk
import threading
import time
import missile
from pygame import mixer
class alien:
    def __init__(self,master,canvas,fenetre,pv,vitesse,position,temps_recharge,etat) -> None:

        self.master=master
        self.canvas=canvas
        self.fenetre=fenetre

        self.pv = pv
        self.vitesse = vitesse
        self.temps_recharge = temps_recharge
        self.etat = etat #mort ou vivant

        self.display_bbox_bool = False
        self.bbox_rect = None

        self.position = position

        self.missiles = []

        self.nom = self.__class__.__name__ #type de l'alien
        self.image = tk.PhotoImage(file=f"images/aliens/{self.nom}.png")
        self.bruitages = {"explosion":mixer.Sound("musiques/bruitages/explosion_alien.mp3")}
    
        self.a_spawn = False # l'alien a t-il spawn ou non

    def collision_missile(self):
        #fonction qui gere la collision entre les missiles et les aliens

        if self.etat == "mort":
            return

        for missile in self.master.vaisseau.missiles:
            missile.nettoyage(self.master.vaisseau) #on profite de la boucle pour nettoyer les missiles qui sont en dehors du canvas
            if missile.etat == "mort":
                continue
            if missile.collision(self):
                self.pv -= 1
                missile.supprimer(self.master.vaisseau)

                score = self.master.score.get()
                self.master.score.set(score+self.score*self.master.niveau.score_multiplieur)

                if self.pv == 0:
                    self.supprimer()
                    break
                    
        self.fenetre.after(50,self.collision_missile)

    def get_bbox(self):
        #retourne les coordonnees de la bbox de l'alien (hitbox)

        return self.canvas.bbox(self.item)

    def supprimer(self):
        #supprime l'alien en activant les bruitages et les effets visuels

        self.fenetre.after(0,self.bruitages["explosion"].play) #joue le bruitage de l'explosion
        self.etat = "mort" 
        self.master.aliens.remove(self)
        self.canvas.delete(self.item)
        self.exploser() 

    def exploser(self):
        #explose l'alien

        image_explosion = tk.PhotoImage(file="images/aliens/explosion.png")
        image_explosion.img = image_explosion #garde une reference a l'image pour ne pas qu'elle soit supprimée par le garbage collector

        explosion = self.canvas.create_image(self.position[0],self.position[1],image=image_explosion)
        self.canvas.itemconfig(explosion)

        self.fenetre.after(300,lambda: self.canvas.delete(explosion))

    def display_bbox(self):
        #affiche la bbox de l'alien
        if self.display_bbox_bool == False:
            return
        if self.bbox_rectangle != None:
            self.canvas.delete(self.bbox_rectangle)
        bbox = self.get_bbox()
        self.bbox_rectangle = self.canvas.create_rectangle(bbox[0],bbox[1],bbox[2],bbox[3],outline="red")
        self.fenetre.after(50,self.display_bbox)