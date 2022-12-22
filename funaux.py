'''
Codé par RONGERE Julien et Rodde Théophile
Date : 05/12/2022
Version : 1.0
Description : fonctions auxiliaires
'''
import time


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