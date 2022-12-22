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

class alien:
    def __init__(self,master,canvas,fenetre,pv,vitesse,position,temps_recharge,etat) -> None:

        self.master=master
        self.canvas=canvas
        self.fenetre=fenetre

        self.pv = pv
        self.vitesse = vitesse
        self.temps_recharge = temps_recharge
        self.etat = etat #mort ou vivant

        self.position = position

        self.missiles = []
    

    def collision_missile(self):

        if self.etat == "mort":
            return

        for missile in self.master.vaisseau.bullets:
            if missile == None:
                continue
            if missile.collision(self):
                self.pv -= 1
                self.canvas.delete(missile.item)                
                self.master.vaisseau.bullets.remove(missile)
                print("touché")
                if self.pv <= 0:
                    self.canvas.delete(self.item)
                    self.master.aliens.remove(self)
                    self.etat = "mort"
                    
            else:
                pass
        self.fenetre.after(50,self.collision_missile)

    def get_bbox(self):
        return self.canvas.bbox(self.item)