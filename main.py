'''
Codé par : RONGERE Julien et Rodde Théophile
Date : 05/12/2022
Version : 1.0
Description : Ceci est le fichier principal du jeu Space Invaders

'''

#importation des modules
import tkinter as tk
import time
import random
import pandas as pd
import numpy as np

import vaisseau
import alien
import aliens_classes
import missile
import niveau
import funaux
import bonus
import menu

import niveaux_jeu

#Création de la fenêtre
class Application :
    def __init__(self,*args,**kwargs):
        self.fenetre = tk.Tk()
        self.fenetre.title("Space Invaders")
        self.fenetre.geometry("800x550")
        self.fenetre.resizable(width=False, height=False)
        self.fenetre.config(bg='grey')
        self.fenetre.protocol("WM_DELETE_WINDOW", self.quitter)


        self.score = tk.IntVar() #variable du score
        self.score.set(0)
        self.der_niveau = 1 #dernier niveau débloqué et non terminé par le joueur

        self.aliens = []
        self.vaisseau = None
        self.bonus = [] #liste des bonus courants
        
        self.init_canvas()
        self.init_boutons()
        self.init_score()
        self.menu = menu.Menu(self,self.canvas,self.fenetre)

        self.fenetre.bind("d",lambda event: self.get_entite(event))

    def get_entite(self,event):
        print(max(funaux.get_entites(self.canvas)),len(funaux.get_entites(self.canvas)))

    #Création du canvas
    def init_canvas(self):
        self.canvas = tk.Canvas(self.fenetre, width=700, height=500, bg='white',highlightthickness=0, relief='ridge')
        self.canvas.place(x=0, y=50)   
        self.fond_canvas = tk.PhotoImage(file="images/fond.png")
        self.canvas.create_image(0,0,anchor="nw",image=self.fond_canvas)
        self.canvas.create_text(350, 250, text="Space Invaders", font=("Arial", 50), fill="red")

    def init_boutons(self):
        #fonction qui initialise les boutons de l'interface

        #boutons pour les 10 niveaux
        self.liste_niveaux = [f"niveaux_jeu.niveau{i}(self,self.canvas,self.fenetre,{i*i})" for i in range(1,11)] #liste des niveaux à instancier
        self.boutton_niveaux_liste = []

        for i in range(1,11):
            self.boutton_niveaux_liste.append(tk.Button(self.fenetre,state="disabled", text="Niveau "+str(i), command= lambda i = i : self.nouvelle_partie(i))) #lambda i = i pour pouvoir passer un argument itéré à la fonction
            self.boutton_niveaux_liste[i-1].place(x=715, y=15+i*35)

        self.boutton_niveaux_liste[0].config(state="normal")
 

    def init_score(self):
        #fonction qui initialise le score

        self.score_label = tk.Label(self.fenetre, text="Score : ")
        self.score_label.place(x=200, y=0)
        self.score_points = tk.Label(self.fenetre, textvariable=self.score)
        self.score_points.place(x=250, y=0)

    def nouvelle_partie(self,niveau=1):
        #fonction qui initialise une nouvelle partie

        for boutton in self.boutton_niveaux_liste: #on désactive tous les bouttons de niveaux pour éviter de lancer plusieurs niveaux en même temps
            boutton.config(state="disabled")
        self.fenetre.after(0,self.menu.supprimer_boutons_accueil)
        self.canvas.delete("all")

        self.niveau_courant = niveau

        self.canvas.create_image(0,0,anchor="nw",image=self.fond_canvas)
        self.vaisseau = vaisseau.vaisseau(self,self.canvas,self.fenetre)
        self.niveau = eval(self.liste_niveaux[niveau-1]) #on instancie le niveau

        self.collision_vaisseau()

    def quitter(self):
        #fonction qui quitte le jeu

        self.fenetre.destroy()  
    
    
    def collision_vaisseau(self):
        #fonction qui vérifie si le vaisseau est en collision avec un alien ou un missile d'alien , et fait le netttoyage des missiles qui sont en dehors du canvas
    
        if self.vaisseau.etat == "mort" or self.vaisseau == None:
            return

        (x1,y1,x2,y2) = self.vaisseau.get_bbox()
        
        for alien in self.aliens:

            if alien.missiles != None:
                
                if alien.etat == "mort" or alien.a_spawn == False or alien==None:
                    continue

                for bullet in alien.missiles: #on vérifie si le vaisseau est en collision avec un missile
                    if bullet.nettoyage(alien) == True: #si le missile est en dehors du canvas, on le supprime
                        continue # et on passe au missile suivant
                    (x3,y3,x4,y4) = bullet.get_bbox()
                    if funaux.rectangle_chevauche((x1,y1,x2,y2),(x3,y3,x4,y4)):

                        if not self.vaisseau.etat == "invincible":
                            self.vaisseau.vie -= 1
                            self.vaisseau.invincible(2)   
                        bullet.supprimer(alien)
                        
                        break
            
            (x3,y3,x4,y4) = alien.get_bbox()  
            if funaux.rectangle_chevauche((x1,y1,x2,y2),(x3,y3,x4,y4)): #on vérifie si le vaisseau est en collision avec un alien
                
                if self.vaisseau.etat == "invincible":

                    alien.supprimer()
                    self.score.set(self.score.get()+1)

                else:
                    alien.supprimer()
                    self.score.set(self.score.get()+alien.score)
                    self.vaisseau.vie -= 1
                    if self.vaisseau.vie <= 0:
                        self.vaisseau.etat = "mort"
                        self.niveau.fin_niveau(False)
                        
                    self.vaisseau.invincible(2)

        self.fenetre.after(50,self.collision_vaisseau)


    def nettoyage_complet(self):
        #fonction qui supprime tous les objets du canvas

        for protection in self.niveau.protections: #on supprime toutes les protections
            if protection != None:
                protection.supprimer()
        self.vaisseau.etat="mort"
        for missile in self.vaisseau.missiles: #on supprime tous les missiles du vaisseau
            missile.supprimer(self.vaisseau)

        for alien in self.aliens:

            [bullets.supprimer(alien) for bullets in alien.missiles] #on supprime tous les missiles des aliens
    
            self.fenetre.after(0,alien.supprimer) #on supprime l'alien

        self.canvas.delete("all")



if __name__ == '__main__':
    app = Application()
    app.fenetre.mainloop()