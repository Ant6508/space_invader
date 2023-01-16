'''
Codé par : RONGERE Julien et Rodde Théophile
Date : 05/12/2022
Version : 1.0
'''

import tkinter as tk
import funaux

class missile:
    def __init__(self,master,canvas,fenetre,position,vitesse) -> None:
        self.master = master
        self.canvas = canvas
        self.fenetre = fenetre
        self.position = position
        self.vitesse = vitesse
        
        self.item = funaux.create_circle(self.position[0],self.position[1],5,self.canvas,fill="red")
        self.etat = "actif"
        self.deplacement()

        self.r = self.canvas.create_rectangle(self.canvas.bbox(self.item),outline="red")
        self.display_bbox()

    def deplacement(self):
        #fonction qui fait déplacer le missile

        if self.etat == "mort":
            return

        self.canvas.move(self.item,self.vitesse[0],self.vitesse[1])
        self.position = self.canvas.coords(self.item)
        if self.etat == "actif":
            self.fenetre.after(100,self.deplacement)

    def nettoyage(self,proprietaire): 
        #fonction qui supprime le missile de la liste des missiles du propriétaire et du canvas si il est hors du canvas

        if self.etat == "mort":
            return False
        if self.position[1] > self.canvas.winfo_height() or self.position[1] < 0 or self.position[0] > self.canvas.winfo_width() or self.position[0] < 0: #si le missile sort de l'écran
            print("missile supprimé : " , self.item)
            self.supprimer(proprietaire)
            return True
        else:
            return False


    def collision(self,objet):
        #fonction qui renvoie True si le missile touche l'objet
        if self.etat == "mort" or objet.etat == "mort" or object==None:
            return False
        (x1,y1,x2,y2) = self.canvas.bbox(objet.item)
        (x3,y3,x4,y4) = self.canvas.bbox(self.item)

        if funaux.rectangle_chevauche((x1,y1,x2,y2),(x3,y3,x4,y4)):
            self.etat = "mort"
            return True
        else:
            return False

    def get_bbox(self):
        return self.canvas.bbox(self.item)


    def display_bbox(self):
        #fonction qui affiche la bbox du missile en rouge

        if self.etat == "mort":
            return

        try:
            self.canvas.delete(self.r)
            self.r = self.canvas.create_rectangle(self.canvas.bbox(self.item),outline="red")
            self.fenetre.after(50,self.display_bbox)

        except:
            pass
    def supprimer(self,proprietaire):
        #fonction qui supprime le missile du canvas et de la liste des missiles du propriétaire
        
        self.etat = "mort"
        self.canvas.delete(self.item)
        self.canvas.delete(self.r)
        proprietaire.missiles.remove(self)