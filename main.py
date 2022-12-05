'''
Codé par : RONGERE Julien et Rodde Théophile
Date : 10/01/2019
Version : 1.0
Description : Space Invaders en tkinter

'''

#importation des modules
import tkinter as tk
import time
import random
import pandas as pd
import numpy as np


#Création de la fenêtre
class Application :
    def __init__(self,*args,**kwargs):
        self.fenetre = tk.Tk()
        self.fenetre.title("Space Invaders")
        self.fenetre.geometry("800x600")
        #self.fenetre.resizable(width=False, height=False)
        self.fenetre.config(bg='grey')
        self.fenetre.protocol("WM_DELETE_WINDOW", self.quitter)
        self.init_canvas()

    #Création du canvas
    def init_canvas(self):
        self.canvas = tk.Canvas(self.fenetre, width=700, height=500, bg='black')
        self.canvas.place(x=50, y=0)   


    def quitter(self):
        self.fenetre.destroy()

if __name__ == '__main__':
    app = Application()
    app.fenetre.mainloop()