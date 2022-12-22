"""
'''
Codé par : RONGERE Julien et Rodde Théophile
Date : 05/12/202
Version : 1.0
Description : Implémentations des aliens
"""

import tkinter as tk
import threading
import time
import missile
import alien
import vaisseau
import funaux

class sbire(alien.alien):
    def __init__(self,master,canvas,fenetre,pv,vitesse,position,temps_recharge,etat) -> None:
        super().__init__(master,canvas,fenetre,pv,vitesse,position,temps_recharge,etat)

        self.pv = pv
        self.vitesse = vitesse
        self.temps_recharge = temps_recharge
        self.image = tk.PhotoImage(file="images/aliens/sbire.png")

        self.score = 10

    def spawn(self):
        print("master : ",self.master,"canvas : ",self.canvas,"fenetre : ",self.fenetre)
        self.item = self.canvas.create_image(self.position[0],self.position[1],image=self.image)
        self.collision_missile()

class shooter(alien.alien):
    def __init__(self,master,canvas,fenetre,pv,vitesse,position,temps_recharge,image,etat) -> None:
        super().__init__(master,canvas,fenetre,pv,vitesse,position,temps_recharge,image,etat)

        self.pv = 1
        self.vitesse = 5
        self.temps_recharge = 1
        self.missiles = []

    def spawn(self):
        self.item = self.canvas.create_image(self.position[0],self.position[1],image=self.image)
        self.collision_missile()
        self.deplacement()
        self.tir()

    def deplacement(self,sens=1):
        if self.etat == "mort":
            return
        self.canvas.move(self.item,self.vitesse*sens,0)
        self.position = (self.position[0]+self.vitesse*sens,self.position[1])
        if self.position[0] > self.canvas.winfo_width() or self.position[0] < 0:
            self.deplacement(-sens)
        else:
            self.fenetre.after(50,self.deplacement,sens)

    def tir(self):
        if self.etat == "mort":
            return
        self.missiles.append(missile.missile(self.master,self.canvas,self.fenetre,self.position,10))
        self.fenetre.after(self.temps_recharge*1000,self.tir)