import math
import turtle 

class Decagon:
    def __init__(self,side):
        self.side = int(side)
        self.corner = 144
        self.K = float(math.sqrt(5 + 2*math.sqrt(5)))

    def opis_okr (self): #Площадь и радиус вписанной оркужности
        self.R = float(((math.sqrt(5) + 1) / 2) * self.side)
        self.S_opis = float((self.R ** 2) * math.pi)
        print("Радиус и площадь окружности описанной в восьмиугольник со стороной",self.side,"равны\n Радиус =",self.R,"\n Площадь =",self.S_opis)

    def vpis_okr (self): #Площадь и радиус вписанной оркужности
        self.r = float((self.K / 2) * self.side)
        self.s_vpis = float((self.r ** 2) * math.pi)
        print("Радиус и площадь окружности вписанной в восьмиугольник со стороной",self.side,"равны\n Радиус =",self.r,"\n Площадь =",self.s_vpis)

    def S_P_dec(self): # Площадь и Периметр восьмиугольника
        self.per_dec = float(self.side*10)
        self.D = float(self.side * self.K)           #расстояние между параллельными сторонами или диаметр вписанной окружности.
        self.s_dec = float((5/2) * self.D * self.side)
        print("Периметр и площадь восьмиугольника со стороной",self.side,"равны\n Периметр =",self.per_dec,"\n Площадь =",self.s_dec)

    def risunok(self): #вывод графика
        self.L = self.R - self.r
        pen = turtle.Turtle()
        pen.color("red")
        pen.circle(self.R, steps=10)
        pen.color("blue")
        pen.circle(self.R)
        pen.color("white")
        pen.left(90)
        pen.forward(self.L)
        pen.right(90)
        pen.color("yellow")
        pen.circle(self.r)

    def __del__(self):
        print("Класс удален")



Ncorner = Decagon(100)
Ncorner.opis_okr()
Ncorner.vpis_okr()
Ncorner.S_P_dec()
Ncorner.risunok()