import niveau
import aliens_classes
from math import sin,cos,pi
import funaux

class niveau1(niveau.niveau):
    def __init__(self,master,canvas,fenetre,score_multiplieur,musique) -> None:

        super().__init__(master,canvas,fenetre,score_multiplieur,musique)

        self.centre_canvas = (self.canvas.winfo_width()/2,self.canvas.winfo_height()/2)
        sbire, shooter = aliens_classes.sbire, aliens_classes.shooter
        position_initiale = (self.centre_canvas[0],self.centre_canvas[1]-100)
        self.aliens_waves = [ [sbire(master,canvas,fenetre,1,10,position_initiale,1,"vivant") for i in range(10)] ]

        self.spawn_aliens()


    def deplacement(self,alien,teta_0 = pi/2):
        #fonction qui fait déplacer l'alien autour de centre centre_canvas et de rayon rayon
        rayon=100
        
        delta_teta = (2*pi)/100

        if alien.etat == "mort":
            return
        pas_x = -alien.position[0]+rayon*cos(teta_0+delta_teta) + self.centre_canvas[0]
        pas_y = -alien.position[1]+rayon*sin(teta_0+delta_teta) + self.centre_canvas[1]
        teta_0 += delta_teta
        alien.canvas.move(alien.item,pas_x,pas_y)
        alien.position = (alien.position[0]+pas_x,alien.position[1]+pas_y)

        self.fenetre.after(50,self.deplacement,alien,teta_0)
