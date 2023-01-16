"""
Codé par : RONGERE Julien et Rodde Théophile
Ce module contient la classe des protections du jeu
"""

import tkinter as tk
import funaux


class protection():
    def __init__(self,master,canvas,fenetre,position,pv) -> None:
        self.master = master
        self.canvas = canvas
        self.fenetre = fenetre
        self.position = position
        self.pv,self.pv_initiale = pv,pv
        self.etat = "vivant" #vivant ou mort

        self.images = {"parfaite":tk.PhotoImage(file="images/protections/0.png"),"endommagee":tk.PhotoImage(file="images/protections/1.png")}

    def collision_missile(self):
        #fonction qui gère la collision entre les missiles des aliens et la protection

        if self.etat == "mort":
            return

        for missile in self.master.vaisseau.missiles:
            if missile.etat == "mort":
                continue
            if missile.collision(self):
                missile.supprimer(self.master.vaisseau)
 

        for alien in self.master.aliens:
            if alien.etat == "mort": #si l'alien est mort, on passe à l'alien suivant
                continue
            for missile in alien.missiles:
                if missile.etat == "mort":
                    continue
                if missile.collision(self):
                    self.pv -= 1
                    missile.supprimer(alien)
                    self.changer_image()

                    if self.pv == 0:
                        self.fenetre.after(50,self.supprimer)
                        
                        break

        self.fenetre.after(50,self.collision_missile)


    def supprimer(self):
        #fonction qui supprime la protection
        
        self.etat = "mort"
        self.canvas.delete(self.item) #on supprime l'image de la protection

    def changer_image(self):
        #fonction qui change l'image de la protection en fonction de ses pv
        if self.etat == "mort":
            return
        if self.pv <= int(self.pv_initiale/2): #si les pv sont à la moitié de ses pv initiaux

            self.canvas.itemconfig(self.item,image=self.images["endommagee"]) #on change son image

    def spawn(self):
        #fonction qui fait spawn la protection
        self.item = self.canvas.create_image(self.position[0],self.position[1],image=self.images["parfaite"]) #on crée l'image de la protection
        self.collision_missile() #on lance la fonction de collision
        self.changer_image()