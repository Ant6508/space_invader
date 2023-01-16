"""
Codé par RONGERE Julien et Rodde Théophile
Date : 11/01/2023
Ce fichier contient la classe bonus qui permet de créer des bonus et d'augmenter les capacités du vaisseau
"""

import tkinter as tk
import time
import random
import funaux


class bonus:
    def __init__(self,master,canvas,fenetre,position,bonus_type) -> None:
        self.master = master
        self.canvas = canvas
        self.fenetre = fenetre
        self.position = position
        self.bonus_type = bonus_type # type de bonus parmis : vie, tir, vitesse
        self.etat = "en_vie" # état du bonus parmis : en_vie, mort

        self.image = tk.PhotoImage(file=f"images/bonus/{self.bonus_type}.png")

    def spawn(self):
        #fonction qui permet de créer le bonus
        self.item = self.canvas.create_image(self.position[0],self.position[1],image=self.image,anchor="nw",tags="bonus")
        self.fenetre.after(50,self.collision)
        self.fenetre.after(50,self.deplacement)
        self.fenetre.after(8000,self.timeout)

    def timeout(self):
        #fonction qui permet de supprimer le bonus après un certain temps
        if self.etat == "mort":
            return
        self.supprimer()

    def collision(self):
        #fonction qui permet de vérifier si le bonus est touché par le vaisseau

        if self.etat == "mort" or self.master.vaisseau.etat == "mort":
            return

        (x1,y1,x2,y2) = self.get_bbox()
        (x3,y3,x4,y4) = self.master.vaisseau.get_bbox()
        if funaux.rectangle_chevauche((x1,y1,x2,y2),(x3,y3,x4,y4)):
       
            self.master.vaisseau.bonus(self.bonus_type)
            self.supprimer()

        self.fenetre.after(50,self.collision)

    def supprimer(self):
        #fonction qui permet de supprimer le bonus

        self.etat = "mort"
        self.canvas.delete(self.item)
        
        
    def deplacement(self):
        #fonction qui permet de faire bouger le bonus aléatoirement
        if self.etat == "mort":
            return
        direction = random.randint(0,3)
        if direction == 0:
            self.canvas.move(self.item,0,-10)
            self.position[1] -= 10
        elif direction == 1:
            self.canvas.move(self.item,0,10)
            self.position[1] += 10
        elif direction == 2:
            self.canvas.move(self.item,-10,0)
            self.position[0] -= 10
        elif direction == 3:
            self.canvas.move(self.item,10,0)
            self.position[0] += 10

    def get_bbox(self):
        #fonction qui permet de récupérer la hitbox du bonus
        return self.canvas.bbox(self.item)