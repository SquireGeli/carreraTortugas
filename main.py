import turtle
import random

class Circuito():
    corredores = []
    _posStartY = (-30,-10,10,30)
    _colorTurtle = ('red','blue','yellow','green')
    def __init__(self,width,height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width,height)
        self.__screen.bgcolor('lightgray')
        self._startline = -width/2 + 20
        self._finishline = width/2 - 20
        
        self._createRunners()
         
     
    def _createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self._colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self._startline, self._posStartY[i])
        
            self.corredores.append(new_turtle)
             
    def competir(self):       
        
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.forward(avance)
                if tortuga.position()[0] >= self._finishline:
                    hayGanador = True
                    print("La tortuga {} HA GANADO!!!".format(tortuga.color()[0]))
        
        
        
if __name__ == '__main__':
    circuito = Circuito (640,480)
    circuito.competir()