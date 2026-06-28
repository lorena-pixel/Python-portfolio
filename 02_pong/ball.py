from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def mover(self):
        nueva_x = self.xcor() + self.x_move
        nueva_y = self.ycor() + self.y_move
        self.goto(nueva_x, nueva_y)

    def rebotar_y(self):
        self.y_move *= -1

    def rebotar_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reiniciar_posicion(self):
        self.goto(0, 0)
        self.move_speed = 0.08
        self.rebotar_x()