import niveau
import aliens_classes
from math import sin,cos,pi
import funaux
from pygame import mixer
class niveau1(niveau.niveau):
    def __init__(self,master,canvas,fenetre,score_multiplieur,musique) -> None:

        super().__init__(master,canvas,fenetre,score_multiplieur,musique)

        self.centre_canvas = (self.canvas.winfo_width()/2,self.canvas.winfo_height()/2)
        sbire, shooter = aliens_classes.sbire, aliens_classes.shooter
        self.position_initiale = (self.centre_canvas[0],self.centre_canvas[1]-150)


        self.aliens_waves = [ [sbire(master,canvas,fenetre,1,10,self.position_initiale,1,"vivant") for i in range(5)] + \
                            [shooter(master,canvas,fenetre,1,10,(100*(i+1),70),1,"vivant") for i in range(3)],
                            [sbire(master,canvas,fenetre,1,10,self.position_initiale,1,"vivant") for i in range(10)] + \
                            [shooter(master,canvas,fenetre,1,10,(100*(i+1),70),1,"vivant") for i in range(5)] ]


        self.fenetre.after(0,self.spawn_aliens)



    def deplacement_sbire(self,alien):
        #fonction qui fait déplacer l'alien autour de centre centre_canvas et de rayon rayon
        teta_0 = pi/2
        delta_teta = pi/100
        funaux.deplacement_circulaire(self.canvas,self.fenetre,alien,100,self.position_initiale,teta_0,delta_teta)
        
    def deplacement_shooter(self,alien,sens=1):
        funaux.deplacement_AR(self.canvas,self.fenetre,alien,sens)
