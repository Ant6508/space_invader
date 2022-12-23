'''
Codé par : RONGERE Julien et Rodde Théophile
Date : 05/12/2022
Version : 1.0
Description : Space Invaders en tkinter

'''

#importation des modules
import tkinter as tk
import time
import random
import pandas as pd
import numpy as np
import vaisseau
import alien
import aliens_examples
import aliens_classes
import missile
import niveau
import niveau1
import funaux

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

        self.aliens = []
        
        self.init_canvas()
        self.init_buttons()
        self.init_score()


    #Création du canvas
    def init_canvas(self):
        self.canvas = tk.Canvas(self.fenetre, width=700, height=500, bg='white',highlightthickness=0, relief='ridge')
        self.canvas.place(x=0, y=50)   
        self.fond_canvas = tk.PhotoImage(file="images/fond.png")
        self.canvas.create_image(0,0,anchor="nw",image=self.fond_canvas)

    def init_buttons(self):
        self.demarrer = tk.Button(self.fenetre, text="Démarrer", command=self.nouvelle_partie)
        self.demarrer.place(x=0, y=0)

    def init_score(self):
        self.score_label = tk.Label(self.fenetre, text="Score : ")
        self.score_label.place(x=200, y=0)
        self.score_points = tk.Label(self.fenetre, textvariable=self.score)
        self.score_points.place(x=250, y=0)

    def nouvelle_partie(self):
        self.canvas.delete("all")
        self.canvas.create_image(0,0,anchor="nw",image=self.fond_canvas)
        self.vaisseau = vaisseau.vaisseau(self,self.canvas,self.fenetre)
        self.niveau1 = niveau1.niveau1(self,self.canvas,self.fenetre,1,"musiques/niveau1.mp3")

        self.collision_vaisseau()

    def spawn(self):
        alien = aliens_examples.alien1(self,self.canvas,self.fenetre,1,50,(100,100),1,tk.PhotoImage(file="images/alien1.png"),"vivant")
        self.aliens.append(alien)
     

    def quitter(self):
        self.fenetre.destroy()  
    
    def tuer_alien(self,alien): #fonction qui tue un alien
        self.aliens.remove(alien)
        self.canvas.delete(alien.item)
        alien.etat = "mort"
  
    
    def collision_vaisseau(self):
        #fonction qui vérifie si le vaisseau est en collision avec un alien ou un missile d'alien
        (x1,y1,x2,y2) = self.vaisseau.get_bbox()
        
        for alien in self.aliens:

            if alien.missiles != None:

                for bullet in alien.missiles: #on vérifie si le vaisseau est en collision avec un missile
                    (x3,y3,x4,y4) = bullet.get_bbox()
                    if funaux.rectangle_chevauche((x1,y1,x2,y2),(x3,y3,x4,y4)):

                        if not self.vaisseau.state == "invincible":
                            self.vaisseau.vie -= 1
                            self.vaisseau.invincible(2)   
                        bullet.supprimer(alien)
                        
                        break

            (x3,y3,x4,y4) = alien.get_bbox()  
            if funaux.rectangle_chevauche((x1,y1,x2,y2),(x3,y3,x4,y4)): #on vérifie si le vaisseau est en collision avec un alien
                
                if self.vaisseau.state == "invincible":

                    self.tuer_alien(alien)
                    self.score.set(self.score.get()+1)

                else:
                    self.tuer_alien(alien)
                    self.score.set(self.score.get()+alien.score)
                    self.vaisseau.vie -= 1
                    if self.vaisseau.vie <= 0:
                        print("Perdu")
                        
                    self.vaisseau.invincible(2)

        self.fenetre.after(50,self.collision_vaisseau)

            
if __name__ == '__main__':
    app = Application()
    app.fenetre.mainloop()
