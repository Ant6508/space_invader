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

class alien1(alien.alien):
    def __init__(self,master,canvas,fenetre,pv,vitesse,position,temps_recharge,image,etat) -> None:
        super().__init__(master,canvas,fenetre,pv,vitesse,position,temps_recharge,image,etat)

        self.pv = 1
        self.vitesse = 10
        self.temps_recharge = 1

        self.deplacement()
   
        
    def deplacement(self):
        if self.etat == "mort":
            return
        self.canvas.move(self.item,0,self.vitesse)
        self.position = (self.position[0],self.position[1]+self.vitesse)
        self.fenetre.after(100,self.deplacement)    
