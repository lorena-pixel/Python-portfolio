from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.puntuacion_izquierda = 0
        self.puntuacion_derecha = 0
        self.actualizar_marcador()

    def actualizar_marcador(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.puntuacion_izquierda, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.puntuacion_derecha, align="center", font=("Courier", 40, "normal"))

    def punto_izquierda(self):
        self.puntuacion_izquierda += 1
        self.actualizar_marcador()

    def punto_derecha(self):
        self.puntuacion_derecha += 1
        self.actualizar_marcador()