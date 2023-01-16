'''
Codé par RONGERE Julien et Rodde Théophile
Date : 05/12/2022
Version : 1.0
Description : Classe du vaisseau du joueur
'''

import tkinter as tk
import time
import random
import pandas as pd
import funaux
import missile
from pygame import mixer
mixer.init()

class vaisseau:

    def __init__(self,master,canvas,fenetre) -> None: #Constructeur
 
        self.master = master
        self.canvas = canvas
        self.fenetre = fenetre

        self.vie = 2
        self.etat = "normal" #normal, invincible, mort
        self.vitesse = 25
        self.position = (150,400)

        self.vitesse_tir = 0.1
        self.en_cooldown = False

        self.image = tk.PhotoImage(file="images/vaisseau.png")
        self.item = canvas.create_image(self.position[0],self.position[1],image=self.image)

        self.fenetre.bind("<Left>",lambda event: self.deplacement(event,-1))
        self.fenetre.bind("<Right>",lambda event: self.deplacement(event,1))
        self.fenetre.bind("<Up>",lambda event: self.deplacement(event,-1))
        self.fenetre.bind("<Down>",lambda event: self.deplacement(event,1))

        self.fenetre.bind("<space>",lambda event: self.tir())
        self.missiles = []
        
        self.r = self.canvas.create_rectangle(self.get_bbox(),outline="red")
        self.display_bbox()

        self.bruitages = {"tir":mixer.Sound("musiques/bruitages/tir_vaisseau.mp3"),"bonus":mixer.Sound("musiques/bruitages/bonus.mp3")}
        self.bruitages["bonus"].set_volume(0.5)
        
    def deplacement(self,event,direction):
        #deplace le vaisseau dans la direction indiquee par la touche pressee
        event = event.keysym
        if event =="Left" or event == "Right":
            if self.position[0] > self.vitesse and direction == -1 and self.position[0] > self.vitesse:
                self.canvas.move(self.item,-self.vitesse,0)
                self.position = (self.position[0]-self.vitesse,self.position[1])
            elif self.position[0] < 700-self.vitesse and direction == 1  and self.position[0] < 700-self.vitesse:
                self.canvas.move(self.item,self.vitesse,0)
                self.position = (self.position[0]+self.vitesse,self.position[1]) 

        elif event == "Up" or event == "Down":
            if self.position[1] > self.vitesse and direction == -1 and self.position[1] > self.vitesse:
                self.canvas.move(self.item,0,-self.vitesse)
                self.position = (self.position[0],self.position[1]-self.vitesse)
            elif self.position[1] < 700-self.vitesse and direction == 1 and self.position[1] < 700-self.vitesse:
                self.canvas.move(self.item,0,self.vitesse)
                self.position = (self.position[0],self.position[1]+self.vitesse)
         

    def invincible(self,time):
        #cree un cercle rouge autour du vaisseau qui le rend invincible pendant un certain temps

        if self.etat == "mort":
            return
        (x1,y1,x2,y2) = self.get_bbox()
        rayon = max(x2-x1,y2-y1)
        self.inv_circle = funaux.create_circle(self.position[0],self.position[1],rayon,self.canvas,outline="red",width=2)
        self.etat = "invincible"
        self.fenetre.after(time*1000,self.invincible_end)


    def invincible_end(self):
        #fin de l'invincibilite
        self.canvas.delete(self.inv_circle)
        self.etat = "normal"


    def get_bbox(self):
        #retourne les coordonnees du rectangle englobant le vaisseau
        return self.canvas.bbox(self.item)

    def display_bbox(self):
        #affiche le rectangle englobant le vaisseau
        if self.etat == "mort":
            return
        self.canvas.delete(self.r)
        self.r = self.canvas.create_rectangle(self.get_bbox(),outline="red")
        self.fenetre.after(100,self.display_bbox)


    def tir(self):
        #fait tirer un missile
        if self.en_cooldown == True:
            return
        self.missiles.append(missile.missile(self.master,self.canvas,self.fenetre,self.position,(0,-20)))
        self.fenetre.after(0,mixer.Sound.play,self.bruitages["tir"])
        self.en_cooldown = True
        self.fenetre.after(int(self.vitesse_tir*1000),self.cooldown_end)
    
    def cooldown_end(self):
        #fin du cooldown
        self.en_cooldown = False

    def bonus(self,bonus_type : str) -> None:
        #fonction appelee lorsqu'un bonus est ramasse
        self.fenetre.after(0,mixer.Sound.play,self.bruitages["bonus"])

        if bonus_type == "vie":
            self.vie += 1
        elif bonus_type == "invincible":
            self.invincible(5)
        elif bonus_type == "vitesse":
            self.vitesse += 5
         
        elif bonus_type == "vitesse_tir":
            if self.vitesse_tir > 0.05:
                self.vitesse_tir -= 0.05
        
        
    def supprimer(self):
        #supprime le vaisseau
        self.canvas.delete(self.item)
        self.canvas.delete(self.r)
        self.etat = "mort"