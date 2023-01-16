"""
Codé par : RONGERE Julien et Rodde Théophile
Ce module contient les classes des niveaux du jeu
"""


import niveau
import aliens_classes
from math import sin,cos,pi
import funaux
from protection import protection

class niveau1(niveau.niveau):
    def __init__(self,master,canvas,fenetre,score_multiplieur) -> None:

        super().__init__(master,canvas,fenetre,score_multiplieur)

        self.centre_canvas = (self.canvas.winfo_width()/2,self.canvas.winfo_height()/2)
        sbire, shooter = aliens_classes.sbire, aliens_classes.shooter
    
        self.aliens_waves = [ [sbire(master,canvas,fenetre,1,10,(100*(i+1),150),1,"vivant") for i in range(6)] + \
                            [shooter(master,canvas,fenetre,1,10,(100*(i+1),70),1,"vivant") for i in range(3)]]

        self.protections = [protection(master,canvas,fenetre,(150 + 100*i,self.canvas.winfo_height()-200),6) for i in range(5)]
        

        self.fenetre.after(0,self.spawn_aliens)


    def deplacement_sbire_0(self,alien):
        #fonction qui fait déplacer de haut en bas l'alien
        funaux.deplacement_AR(self.canvas,self.fenetre,alien,1,False)

    def deplacement_shooter_0(self,alien,sens=1):
        #fonction qui fait déplacer de gauche à droite l'alien
        funaux.deplacement_AR(self.canvas,self.fenetre,alien,-1,True)


class niveau2(niveau.niveau):
    def __init__(self,master,canvas,fenetre,score_multiplieur) -> None:

        super().__init__(master,canvas,fenetre,score_multiplieur)

        self.centre_canvas = (self.canvas.winfo_width()/2,self.canvas.winfo_height()/2)
        sbire, shooter = aliens_classes.sbire, aliens_classes.shooter
        self.position_initiale = (self.centre_canvas[0],self.centre_canvas[1]-150)

        self.aliens_waves = [ [sbire(master,canvas,fenetre,1,10,self.position_initiale,1,"vivant") for i in range(10)] + \
                            [shooter(master,canvas,fenetre,1,10,(100*(i+1),70),1,"vivant") for i in range(5)],

                            [sbire(master,canvas,fenetre,2,10,self.position_initiale,1,"vivant") for i in range(20)] + \
                            [shooter(master,canvas,fenetre,2,15,(100*(i+1),70),0.7,"vivant") for i in range(5)] ]


        self.protections = [protection(master,canvas,fenetre,(150 + 100*i,self.canvas.winfo_height()-200),6) for i in range(5)]

        self.fenetre.after(0,self.spawn_aliens)


    def deplacement_sbire_0(self,alien):
        #fonction qui fait déplacer l'alien autour de centre centre_canvas et de rayon 200
        teta_0 = pi/2
        delta_teta = pi/100
        funaux.deplacement_circulaire(self.canvas,self.fenetre,alien,200,self.centre_canvas,teta_0,delta_teta)
        
    def deplacement_shooter_0(self,alien,sens=1):
        funaux.deplacement_AR(self.canvas,self.fenetre,alien,-1,True)


class niveau3(niveau.niveau):
    def __init__(self,master,canvas,fenetre,score_multiplieur) -> None:
        super().__init__(master,canvas,fenetre,score_multiplieur)
    
        sbire,shooter,soldat = aliens_classes.sbire,aliens_classes.shooter,aliens_classes.soldat

    
        self.aliens_waves = [ [sbire(master,canvas,fenetre,1,10,(100,100),1,"vivant") for i in range(6)] + \
                            [shooter(master,canvas,fenetre,1,10,(100*(i+1),70),1,"vivant") for i in range(3)] + \
                            [soldat(master,canvas,fenetre,1,3,(0,0),1,"vivant") for i in range(3)] + \
                            [soldat(master,canvas,fenetre,1,3,(600,0),1,"vivant") for i in range(3)] ,

                            [sbire(master,canvas,fenetre,2,13,(100,100),1,"vivant") for i in range(6)] + \
                            [shooter(master,canvas,fenetre,1,13,(100*(i+1),70),1,"vivant") for i in range(3)] + \
                            [soldat(master,canvas,fenetre,1,4,(0,0),1,"vivant") for i in range(5)] + \
                            [soldat(master,canvas,fenetre,1,4,(600,0),1,"vivant") for i in range(5)] ,                

                            [sbire(master,canvas,fenetre,2,13,(100,100),1,"vivant") for i in range(6)] + \
                            [shooter(master,canvas,fenetre,2,13,(100*(i+1),70),1,"vivant") for i in range(6)] + \
                            [soldat(master,canvas,fenetre,1,4,(0,0),1,"vivant") for i in range(5)] + \
                            [soldat(master,canvas,fenetre,1,4,(600,0),1,"vivant") for i in range(5)] 

                            ]


                            
        self.fenetre.after(0,self.spawn_aliens)

    def deplacement_sbire_0(self,alien):
        funaux.deplacement_AR_descente(self.canvas,self.fenetre,alien,1)

    def deplacement_shooter_0(self,alien):
        funaux.deplacement_AR(self.canvas,self.fenetre,alien,1,True)

    def deplacement_soldat_0(self,alien):
        alien.deplacement()

class niveau4(niveau.niveau):
    def __init__(self,master,canvas,fenetre,score_multiplieur) -> None:
        super().__init__(master,canvas,fenetre,score_multiplieur)

        self.centre_canvas = (self.canvas.winfo_width()/2,self.canvas.winfo_height()/2)

        sbire,shooter,soldat,boss1 = aliens_classes.sbire,aliens_classes.shooter,aliens_classes.soldat,aliens_classes.boss1

        self.aliens_waves = [ [sbire(master,canvas,fenetre,5,10,(self.centre_canvas[0],self.centre_canvas[1]-150),1,"vivant") for i in range(15)] + \
                            [shooter(master,canvas,fenetre,2,10,(self.centre_canvas[0],self.centre_canvas[1]-100),1,"vivant") for i in range(10)] + \
                            [boss1(master,canvas,fenetre,14,15,self.centre_canvas,1,"vivant")],

                            [sbire(master,canvas,fenetre,8,10,(self.centre_canvas[0],self.centre_canvas[1]-150),1,"vivant") for i in range(20)] + \
                            [shooter(master,canvas,fenetre,4,10,(self.centre_canvas[0],self.centre_canvas[1]-100),0.8,"vivant") for i in range(10)] + \
                            [boss1(master,canvas,fenetre,17,15,self.centre_canvas,1,"vivant")] +\
                            [soldat(master,canvas,fenetre,1,3,(0,0),1,"vivant") for i in range(3)] + \
                            [soldat(master,canvas,fenetre,1,3,(600,0),1,"vivant") for i in range(3)] +\
                            [boss1(master,canvas,fenetre,12,20,self.centre_canvas,1,"vivant")],

                            [sbire(master,canvas,fenetre,8,10,(self.centre_canvas[0],self.centre_canvas[1]-150),1,"vivant") for i in range(20)] + \
                            [shooter(master,canvas,fenetre,4,10,(self.centre_canvas[0],self.centre_canvas[1]-100),0.7,"vivant") for i in range(10)] + \
                            [boss1(master,canvas,fenetre,17,15,self.centre_canvas,1,"vivant")] +\
                            [soldat(master,canvas,fenetre,1,4,(0,0),1,"vivant") for i in range(5)] + \
                            [soldat(master,canvas,fenetre,1,4,(600,0),1,"vivant") for i in range(5)] 
                            ]



        self.fenetre.after(0,self.spawn_aliens)


    def deplacement_sbire_0(self,alien):
        funaux.deplacement_circulaire(self.canvas,self.fenetre,alien,150,self.centre_canvas,pi/2,pi/100)

    def deplacement_shooter_0(self,alien):
        funaux.deplacement_circulaire(self.canvas,self.fenetre,alien,100,self.centre_canvas,pi/2,pi/100)

    def deplacement_boss1_0(self,alien):
        #le boss possède déjà une fonction de déplacement
        pass

    def deplacement_soldat_0(self,alien):
        alien.deplacement()
    
class niveau5(niveau.niveau):
    def __init__(self,master,canvas,fenetre,score_multiplieur) -> None:
        super().__init__(master,canvas,fenetre,score_multiplieur)

        self.centre_canvas = (self.canvas.winfo_width()/2,self.canvas.winfo_height()/2)

        sbire,shooter,soldat,boss2 = aliens_classes.sbire,aliens_classes.shooter,aliens_classes.soldat,aliens_classes.boss2

        self.aliens_waves = [ [sbire(master,canvas,fenetre,5,10,(100,50),1,"vivant") for i in range(6)] + \
                            [shooter(master,canvas,fenetre,2,10,(self.centre_canvas[0],self.centre_canvas[1]-150),1,"vivant") for i in range(10)] + \
                            [boss2(master,canvas,fenetre,14,15,self.centre_canvas,1,"vivant")],

                            [sbire(master,canvas,fenetre,8,10,(100,50),1,"vivant") for i in range(10)] + \
                            [shooter(master,canvas,fenetre,4,10,(self.centre_canvas[0],self.centre_canvas[1]-150),0.8,"vivant") for i in range(10)] + \
                            [boss2(master,canvas,fenetre,17,15,self.centre_canvas,1,"vivant")] +\
                            [soldat(master,canvas,fenetre,3,3,(0,0),1,"vivant") for i in range(3)] + \
                            [soldat(master,canvas,fenetre,3,3,(600,0),1,"vivant") for i in range(3)],

                            [sbire(master,canvas,fenetre,8,15,(100,50),1,"vivant") for i in range(10)] + \
                            [shooter(master,canvas,fenetre,4,15,(self.centre_canvas[0],self.centre_canvas[1]-100),0.7,"vivant") for i in range(15)] + \
                            [boss2(master,canvas,fenetre,17,15,self.centre_canvas,1,"vivant")] +\
                            [soldat(master,canvas,fenetre,1,4,(0,0),1,"vivant") for i in range(5)] + \
                            [soldat(master,canvas,fenetre,1,4,(600,0),1,"vivant") for i in range(5)],

                            [shooter(master,canvas,fenetre,4,15,(self.centre_canvas[0],self.centre_canvas[1]-100),0.7,"vivant") for i in range(15)] + \
                            [boss2(master,canvas,fenetre,17,15,self.centre_canvas,1,"vivant") for i in range(3)] +\
                            [soldat(master,canvas,fenetre,1,5,(0,0),1,"vivant") for i in range(5)] + \
                            [soldat(master,canvas,fenetre,1,5,(600,0),1,"vivant") for i in range(5)],
                            ]

        self.protections = [protection(self.master,self.canvas,self.fenetre,(self.centre_canvas[0],self.centre_canvas[1]+100),10) for i in range(3)]
        self.fenetre.after(0,self.spawn_aliens)

    def deplacement_sbire_0(self,alien):
        funaux.deplacement_AR(self.canvas,self.fenetre,alien,1,False,self.canvas.winfo_width())

    def deplacement_shooter_0(self,alien):
        funaux.deplacement_AR(self.canvas,self.fenetre,alien,1,True)

    def deplacement_boss2_0(self,alien):
        funaux.deplacement_circulaire(self.canvas,self.fenetre,alien,150,self.centre_canvas,pi/2,pi/100)
class niveau6:
    def __init__(self,master,canvas,fenetre,score_multiplieur) -> None:
        pass
class niveau7:
    def __init__(self,master,canvas,fenetre,score_multiplieur) -> None:
        pass
class niveau8:
    def __init__(self,master,canvas,fenetre,score_multiplieur) -> None:
        pass
class niveau9:
    def __init__(self,master,canvas,fenetre,score_multiplieur) -> None:
        pass
class niveau10:
    def __init__(self,master,canvas,fenetre,score_multiplieur) -> None:
        pass