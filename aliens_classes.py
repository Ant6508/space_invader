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
import random

class sbire(alien.alien):
    def __init__(self,master,canvas,fenetre,pv,vitesse,position,temps_recharge,etat) -> None:
        super().__init__(master,canvas,fenetre,pv,vitesse,position,temps_recharge,etat)

        self.pv = pv
        self.vitesse = vitesse
        self.temps_recharge = temps_recharge
        self.image = tk.PhotoImage(file="images/aliens/sbire.png")

        self.score = 10

    def spawn(self):
        self.item = self.canvas.create_image(self.position[0],self.position[1],image=self.image)
        self.collision_missile()

class shooter(alien.alien):
    def __init__(self,master,canvas,fenetre,pv,vitesse,position,temps_recharge,etat) -> None:
        super().__init__(master,canvas,fenetre,pv,vitesse,position,temps_recharge,etat)

        self.score = 20

    def spawn(self):
        #fonction qui spawn l'alien

        self.item = self.canvas.create_image(self.position[0],self.position[1],image=self.image)
        self.collision_missile()
        self.tir()

    def tir(self):
        if self.etat == "mort":
            return
        self.missiles.append(missile.missile(self.master,self.canvas,self.fenetre,self.position,(0,10)))
        self.fenetre.after(int(self.temps_recharge*1000),self.tir)


class soldat(alien.alien):
    def __init__(self,master,canvas,fenetre,pv,vitesse,position,temps_recharge,etat) -> None:
        super().__init__(master,canvas,fenetre,pv,vitesse,position,temps_recharge,etat) 

        self.score = 30

    def spawn(self):
        self.item = self.canvas.create_image(self.position[0],self.position[1],image=self.image)
        self.collision_missile()

    def deplacement(self):
        if self.etat == "mort":
            return
        position_vaisseau = self.master.vaisseau.position
        #deplacement vers le vaisseau
        if position_vaisseau[0] > self.position[0]:
            self.position = (self.position[0] + self.vitesse,self.position[1])
        elif position_vaisseau[0] < self.position[0]:
            self.position = (self.position[0] - self.vitesse,self.position[1])
        if position_vaisseau[1] > self.position[1]:
            self.position = (self.position[0],self.position[1] + self.vitesse)
        elif position_vaisseau[1] < self.position[1]:
            self.position = (self.position[0],self.position[1] - self.vitesse) 

        self.canvas.coords(self.item,self.position[0],self.position[1])

        self.fenetre.after(50,self.deplacement)

class boss1(alien.alien):
    def __init__(self, master, canvas, fenetre, pv, vitesse, position, temps_recharge, etat) -> None:
        super().__init__(master, canvas, fenetre, pv, vitesse, position, temps_recharge, etat)

        self.score = 200

    def spawn(self):
        self.item = self.canvas.create_image(self.position[0],self.position[1],image=self.image)
        self.collision_missile()
        self.deplacement()

    def deplacement(self):
        #fonction qui fait bouger l'alien de maniere aleatoire
        if self.etat == "mort":
            return
        self.position = (self.position[0] + random.randint(-self.vitesse,self.vitesse),self.position[1] + random.randint(-self.vitesse,self.vitesse))
        if self.position[0] < 0:
            self.position = (0,self.position[1])
        elif self.position[0] > self.fenetre.winfo_width():
            self.position = (self.fenetre.winfo_width()-50,self.position[1])
        if self.position[1] < 0:
            self.position = (self.position[0],0)
        elif self.position[1] > self.fenetre.winfo_height():
            self.position = (self.position[0],self.fenetre.winfo_height()-50)
        self.canvas.coords(self.item,self.position[0],self.position[1])
        self.fenetre.after(50,self.deplacement)


class boss2(alien.alien):
    def __init__(self, master, canvas, fenetre, pv, vitesse, position, temps_recharge, etat) -> None:
        super().__init__(master, canvas, fenetre, pv, vitesse, position, temps_recharge, etat)

        self.score = 250

    def spawn(self):
        #fonction qui spawn l'alien
        
        self.item = self.canvas.create_image(self.position[0],self.position[1],image=self.image)
        self.collision_missile()
        self.invisible()

    def invisible(self): 
        #fonction qui fait disparaitre l'alien pendant 2 secondes

        if self.etat == "mort":
            return
        self.canvas.itemconfig(self.item,state="hidden")
        self.fenetre.after(2000,lambda : self.canvas.itemconfig(self.item,state="normal"))
        self.fenetre.after(3000,self.invisible)

class boss3(alien.alien):
    def __init__(self, master, canvas, fenetre, pv, vitesse, position, temps_recharge, etat) -> None:
        super().__init__(master, canvas, fenetre, pv, vitesse, position, temps_recharge, etat)

        self.score = 300

    def spawn(self):
        #fonction qui spawn l'alien

        self.item = self.canvas.create_image(self.position[0],self.position[1],image=self.image)
        self.collision_missile()
        self.tir()

    def tir(self):
        #fonction qui fait tirer l'alien 3 missiles

        if self.etat == "mort":
            return
        self.missiles.append(missile.missile(self.master,self.canvas,self.fenetre,self.position,(0,10)))
        self.missiles.append(missile.missile(self.master,self.canvas,self.fenetre,self.position,(-2,10)))
        self.missiles.append(missile.missile(self.master,self.canvas,self.fenetre,self.position,(2,10)))

        self.fenetre.after(int(self.temps_recharge*1000),self.tir)