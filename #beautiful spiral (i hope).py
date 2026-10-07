#beautiful spiral (i hope)

import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("color spiral")

t = turtle.Turtle()
t.speed(0)
turtle.tracer(2)
t.hideturtle()

total = 0 #ca va nous aider à changer la couleur

for i in range (0,500):
    color = colorsys.hsv_to_rgb(total,1,1)
    t.pencolor(color)
    t.forward(i+4)
    t.right(121) #angle rotation effet carré décalé
    total +=0.005

t.up()
# Forcer le rafraîchissement final de l'affichage
turtle.update()

# Conserver la fenêtre ouverte jusqu'à ce qu'elle soit fermée manuellement
turtle.done()
