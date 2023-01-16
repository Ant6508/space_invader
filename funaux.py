'''
Codé par RONGERE Julien et Rodde Théophile
Date : 05/12/2022
Version : 1.0
Description : fonctions auxiliaires utiles au projet
'''
import time
from math import cos,sin

def exec_fonction_temps(fonction,duree,delai=100):
    #fonction qui exécute la fonction fonction pendant duree secondes avec un délai den millisecondes entre chaque exécution
    depart = time.time()
    while time.time() - depart < duree:
        fonction()
        time.sleep(delai/1000)
        
def create_circle(x, y, r,canvas, **kwargs):
    #fonction qui crée un cercle de centre (x,y) et de rayon r sur le canvas canvasName

    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def rectangle_chevauche(rect1,rect2):
    #fonction qui renvoie True si les rectangles rect1 et rect2 se chevauchent, False sinon

    (x1,y1,x2,y2) = rect1
    (x3,y3,x4,y4) = rect2
    if (x1 <= x3 <= x2 or x1 <= x4 <= x2) and (y1 <= y3 <= y2 or y1 <= y4 <= y2):
        return True
    else:
        return False

def ajoute_aliens(master,aliens_waves):
    #fonction qui ajoute les aliens à la liste des aliens du master

    for wave in aliens_waves:
        for alien in wave:
            master.aliens.append(alien)

#fonctions pour déplacer les aliens

def deplacement_circulaire(canvas,fenetre,alien,rayon,centre,teta_0,delta_teta):
    #déplacement circulaire  de centre centre, de rayon rayon, d'angle initalie teta0, de variation d'angle delta_teta

    if alien.etat == "mort": #si l'alien est mort, on ne fait rien
        return

    pas_x = -alien.position[0]+rayon*cos(teta_0+delta_teta) + centre[0] #on calcule le déplacement à effectuer
    pas_y = -alien.position[1]+rayon*sin(teta_0+delta_teta) + centre[1]

    teta_0 += delta_teta #on incrémente l'angle
    canvas.move(alien.item,pas_x,pas_y) #on déplace l'alien
    alien.position = (alien.position[0]+pas_x,alien.position[1]+pas_y)  #on met à jour la position de l'alien

    fenetre.after(50,deplacement_circulaire,canvas,fenetre,alien,rayon,centre,teta_0,delta_teta) #on rappelle la fonction après 50ms

def deplacement_AR(canvas,fenetre,alien,sens,bool_horizontale,y_min=300): #déplacement aller-retour
    #le paramètre bool_horizontale permet de savoir si l'alien se déplace horizontalement ou verticalement

    if alien.etat == "mort": #si l'alien est mort, on ne fait rien
        return

    if bool_horizontale: #si l'alien se déplace horizontalement
        h,v=1,0
    else: #si l'alien se déplace verticalement
        h,v=0,1

    canvas.move(alien.item,alien.vitesse*sens*h,alien.vitesse*sens*v) #on déplace l'alien
    alien.position = (alien.position[0]+alien.vitesse*sens*h,alien.position[1]+alien.vitesse*sens*v) #on met à jour la position de l'alien

    if (alien.position[0] + alien.vitesse*sens >= canvas.winfo_width() or alien.position[0] + alien.vitesse*sens <= 0) and bool_horizontale : #si l'alien touche un bord, on change de sens
        sens *= -1

    if( alien.position[1] + alien.vitesse*sens <= 0 or alien.position[1] + alien.vitesse*sens >= y_min) and not ( bool_horizontale ):
        sens *= -1

    fenetre.after(50,deplacement_AR,canvas,fenetre,alien,sens,bool_horizontale,y_min) #on rappelle la fonction après 50ms

def deplacement_AR_descente(canvas,fenetre,alien,sens):
    #fonction qui permet de faire descendre l'alien en même temps qu'il se déplace horizontalement

    deplacement_AR(canvas,fenetre,alien,sens,True,canvas.winfo_height())
    if alien.position[0] + alien.vitesse*sens >= canvas.winfo_width() or alien.position[0] + alien.vitesse*sens <= 0:
        canvas.move(alien.item,0,alien.vitesse)
        alien.position = (alien.position[0],alien.position[1]+alien.vitesse)

    if alien.position[1] >= canvas.winfo_height(): #si l'alien touche le bas de l'écran, on le fait réapparaître en haut
        canvas.move(alien.item,0,-canvas.winfo_height())
        alien.position = (alien.position[0],0)

def get_entites(canvas,*args):
    #fonction qui renvoie la liste des entités du canvas

    liste_entites = canvas.find_all()
    return liste_entites