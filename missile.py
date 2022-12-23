'''
Codé par : RONGERE Julien et Rodde Théophile
Date : 05/12/2022
Version : 1.0
'''

import tkinter as tk
import funaux

class missile:
    def __init__(self,master,canvas,fenetre,position,vitesse) -> None:
        self.master = master
        self.canvas = canvas
        self.fenetre = fenetre
        self.position = position
        self.vitesse = vitesse
        
        self.item = funaux.create_circle(self.position[0],self.position[1],5,self.canvas,fill="red")
        self.etat = "actif"
        self.deplacement()

        self.r = self.canvas.create_rectangle(self.canvas.bbox(self.item),outline="red")
        self.display_bbox()

    def deplacement(self):
        self.canvas.move(self.item,0,self.vitesse)
        self.position = (self.position[0],self.position[1]+self.vitesse)
        if self.etat == "actif":
            self.fenetre.after(100,self.deplacement)

    def nettoyage(self): 
        if self.position[1] > self.canvas.winfo_height():
            self.etat = "mort"
            self.canvas.delete(self.item)
        else:
            self.fenetre.after(100,self.nettoyage)

    def collision(self,objet):
        #fonction qui renvoie True si le missile touche l'objet
        if self.etat == "mort" or objet.etat == "mort":
            return False
        (x1,y1,x2,y2) = self.canvas.bbox(objet.item)
        (x3,y3,x4,y4) = self.canvas.bbox(self.item)

        if funaux.rectangle_chevauche((x1,y1,x2,y2),(x3,y3,x4,y4)):
            print("collision")
            return True
        else:
            return False

    def get_bbox(self):
        return self.canvas.bbox(self.item)


    def display_bbox(self):
        if self.etat == "mort":
            return
        self.canvas.delete(self.r)
        self.r = self.canvas.create_rectangle(self.canvas.bbox(self.item),outline="red")
        self.fenetre.after(100,self.display_bbox)

    def supprimer(self,proprietaire):
        self.etat = "mort"
        self.canvas.delete(self.item)
        self.canvas.delete(self.r)
        proprietaire.missiles.remove(self)