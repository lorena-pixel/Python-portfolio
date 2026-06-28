from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


pantalla = Screen()
pantalla.setup(width=800, height=600)
pantalla.bgcolor("black")
pantalla.title("Pong")
pantalla.tracer(0)

paddle_derecha = Paddle((350, 0))
paddle_izquierda = Paddle((-350, 0))
pelota = Ball()
marcador = Scoreboard()

pantalla.listen()
pantalla.onkey(paddle_derecha.subir, "Up")
pantalla.onkey(paddle_derecha.bajar, "Down")
pantalla.onkey(paddle_izquierda.subir, "w")
pantalla.onkey(paddle_izquierda.bajar, "s")

juego_activo = True

while juego_activo:
    time.sleep(pelota.move_speed)
    pantalla.update()
    pelota.mover()

    if pelota.ycor() > 280 or pelota.ycor() < -280:
        pelota.rebotar_y()

    if pelota.distance(paddle_derecha) < 50 and pelota.xcor() > 320:
        pelota.rebotar_x()

    if pelota.distance(paddle_izquierda) < 50 and pelota.xcor() < -320:
        pelota.rebotar_x()

    if pelota.xcor() > 380:
        pelota.reiniciar_posicion()
        marcador.punto_izquierda()

    if pelota.xcor() < -380:
        pelota.reiniciar_posicion()
        marcador.punto_derecha()

pantalla.exitonclick()