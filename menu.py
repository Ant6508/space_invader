"""
Codé par : RONGERE Julien et Rodde Théophile
Date : 11/01/2023
Ce fichier contient la classe menu qui permet de créer le menu du jeu
"""

import tkinter as tk
from tkinter import simpledialog

class Menu:
    def __init__(self,master,canvas,fenetre) -> None:
        self.master = master
        self.canvas = canvas
        self.fenetre = fenetre

        self.init_menu_accueil()

    def init_boutons_accueil(self):
        #fonction qui permet de créer les boutons du menu

        self.bouton_jouer = tk.Button(self.canvas,text="Jouer",command=self.jouer,width=20,height=5)
        self.bouton_jouer.place(x=100,y=100)

        self.bouton_quitter = tk.Button(self.canvas,text="Quitter",command=self.quitter)
        self.bouton_quitter.place(x=100,y=200)
        
    def init_menu_accueil(self):
        #fonction qui permet de créer le menu d'accueil
        self.canvas.create_image(0,0,anchor="nw",image=self.master.fond_canvas)
        self.canvas.create_text(350,50,text="Space Invaders",font=("Arial",30),fill="red")
        self.init_boutons_accueil()


    def jouer(self):
        #fonction qui permet de lancer le dernier niveau debloque du jeu

        self.master.nouvelle_partie(self.master.der_niveau)

    def entrer_code(self):
        #fonction qui permet au joueur d'entrer un code

        code = simpledialog.askstring("Entrer un code","Entrer un code")

        if code == "CPE4LIFE":
            self.master.vaisseau.vie = 100
        elif code == "END":
            if all([alien.a_spawn for alien in self.master.niveau.aliens_waves[self.master.niveau.vague_courante]]): #si tous les aliens ont spawn
            
                self.master.der_niveau = 10  #on débloque tous les niveaux
                self.master.niveau.fin_niveau(True) #la partie s'arrête

        elif code =="superman":
            self.master.vaisseau.etat = "invincible"

    def quitter(self):
        #fonction qui permet de quitter le jeu

        self.fenetre.destroy()

    
    def supprimer_boutons_accueil(self):
        #fonction qui permet de supprimer les boutons du menu
        self.bouton_jouer.destroy()
 
        self.bouton_quitter.destroy()