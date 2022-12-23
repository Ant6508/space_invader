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

class vaisseau:

    def __init__(self,master,canvas,fenetre) -> None: #Constructeur
 
        self.master = master
        self.canvas = canvas
        self.fenetre = fenetre

        self.vie = 2
        self.state = "normal" #normal, invincible, dead
        self.vitesse = 25
        self.position = (150,400)

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

    def deplacement(self,event,direction):
        #deplace le vaisseau dans la direction indiquee par la touche pressee
        event = event.keysym
        if event =="Left" or event == "Right":
            if self.position[0] > self.vitesse and direction == -1:
                self.canvas.move(self.item,-self.vitesse,0)
                self.position = (self.position[0]-self.vitesse,self.position[1])
            elif self.position[0] < 700-self.vitesse and direction == 1:
                self.canvas.move(self.item,self.vitesse,0)
                self.position = (self.position[0]+self.vitesse,self.position[1]) 

        elif event == "Up" or event == "Down":
            if self.position[1] > self.vitesse and direction == -1:
                self.canvas.move(self.item,0,-self.vitesse)
                self.position = (self.position[0],self.position[1]-self.vitesse)
            elif self.position[1] < 700-self.vitesse and direction == 1:
                self.canvas.move(self.item,0,self.vitesse)
                self.position = (self.position[0],self.position[1]+self.vitesse)
         
    

    def invincible(self,time,sens=-1):
        #cree un cercle rouge autour du vaisseau qui le rend invincible pendant un certain temps

        self.inv_circle = funaux.create_circle(self.position[0],self.position[1],max(self.get_bbox()),self.canvas,outline="red",width=2)
        self.state = "invincible"
        self.fenetre.after(time*1000,self.invincible_end)


    def invincible_end(self):
        #fin de l'invincibilite
        self.canvas.delete(self.inv_circle)
        self.state = "normal"


    def get_bbox(self):
        #retourne les coordonnees du rectangle englobant le vaisseau
        return self.canvas.bbox(self.item)

    def display_bbox(self):
        #affiche le rectangle englobant le vaisseau
        self.canvas.delete(self.r)
        self.r = self.canvas.create_rectangle(self.get_bbox(),outline="red")
        self.fenetre.after(100,self.display_bbox)


    def tir(self):
        #fait tirer un missile
        self.missiles.append(missile.missile(self.master,self.canvas,self.fenetre,self.position,-20))

    

        