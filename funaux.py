'''
Codé par RONGERE Julien et Rodde Théophile
Date : 05/12/2022
Version : 1.0
Description : fonctions auxiliaires
'''
import time
from math import cos,sin

def exec_fonction_temps(fonction,duree,delai=100):
    '''
    Fonction qui execute une fonction pendant un certain temps
    '''
    depart = time.time()
    while time.time() - depart < duree:
        fonction()
        time.sleep(delai/1000)
        
def create_circle(x, y, r, canvasName, **kwargs):
    return canvasName.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def rectangle_chevauche(rect1,rect2):
    '''
    Fonction qui renvoie True si les deux rectangles se chevauchent
    '''
    (x1,y1,x2,y2) = rect1
    (x3,y3,x4,y4) = rect2
    if (x1 <= x3 <= x2 or x1 <= x4 <= x2) and (y1 <= y3 <= y2 or y1 <= y4 <= y2):
        return True
    else:
        return False

def ajoute_aliens(master,aliens_waves):
    for wave in aliens_waves:
        for alien in wave:
            master.aliens.append(alien)

#fonctions pour déplacer les aliens

def deplacement_circulaire(canvas,fenetre,alien,rayon,centre,teta_0,delta_teta): #déplacement circulaire 

    if alien.etat == "mort": #si l'alien est mort, on ne fait rien
        return

    pas_x = -alien.position[0]+rayon*cos(teta_0+delta_teta) + centre[0] #on calcule le déplacement à effectuer
    pas_y = -alien.position[1]+rayon*sin(teta_0+delta_teta) + centre[1]

    teta_0 += delta_teta #on incrémente l'angle
    canvas.move(alien.item,pas_x,pas_y) #on déplace l'alien
    alien.position = (alien.position[0]+pas_x,alien.position[1]+pas_y)  #on met à jour la position de l'alien

    fenetre.after(50,deplacement_circulaire,canvas,fenetre,alien,rayon,centre,teta_0,delta_teta) #on rappelle la fonction après 50ms

def deplacement_AR(canvas,fenetre,alien,sens): #déplacement aller-retour

    if alien.etat == "mort": #si l'alien est mort, on ne fait rien
        return

    canvas.move(alien.item,alien.vitesse*sens,0) #on déplace l'alien
    alien.position = (alien.position[0]+alien.vitesse*sens,alien.position[1]) #on met à jour la position de l'alien

    if alien.position[0] + alien.vitesse >= canvas.winfo_width() or alien.position[0] + alien.vitesse <= 0: #si l'alien touche un bord, on change de sens
        sens *= -1
    fenetre.after(50,deplacement_AR,canvas,fenetre,alien,sens) #on rappelle la fonction après 50ms