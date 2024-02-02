from turtle import *
from math import sqrt, sin, pi, atan, degrees
franklin = Turtle()

franklin.shape("turtle")
franklin.color("#0033CC")
franklin.speed(0)
franklin.down()


#écrire une fct python pour que la tortue dessine un carré
def carre(cote):
    for _ in range(4):
        franklin.forward(cote)
        franklin.left(90)

#carre(200) #appel a la fonction carre
def carre_tournant(n,cote):
    #angle de rotation de 71,56°
    #raison géométrique de sqrt(10)/4   
    if n == 1:
        carre(cote)
        franklin.hideturtle()
    else:
        if n % 2 == 0:
            franklin.color("blue")
            franklin.fillcolor("blue")
        else:
            franklin.color("red")
            franklin.fillcolor("red")
        nv_cote = int(cote*sqrt(10)/4)
        carre(nv_cote)
        franklin.forward(int((nv_cote)*3/4))
        franklin.left(degrees(atan(3)))
        carre_tournant(n-1,int(nv_cote))

#carre_tournant(10,300) #appel a la fonction carre_tournant avec n = 10 et cote = 300

#complet
def vonkoch(n,cote):
    if n == 1:
        franklin.forward(cote)
        franklin.hideturtle()
    else:
        cote = cote//3
        vonkoch(n-1,cote)
        franklin.left(60)
        vonkoch(n-1,cote)
        franklin.right(120)
        vonkoch(n-1,cote)
        franklin.left(60)
        vonkoch(n-1,cote)
#vonkoch(5,300) # appel a la fonction vonkoch avec n = 5 et cote = 300

def von_koch(n,cote):
    if n == 0:
        franklin.forward(cote)
    else:
        cote = cote // 3
        von_koch(n-1,cote)
        franklin.lt(60)
        von_koch(n-1,cote)
        franklin.rt(120)
        von_koch(n-1,cote)
        franklin.lt(60)
        von_koch(n-1,cote)
        franklin.hideturtle()
        
        
#von_koch(5,300) # appel a la fonction von_koch avec n = 5 et cote = 300

def flocon(n, cote):
    for _ in range(3):
        vonkoch(n,cote)
        franklin.rt(120)
        
#flocon(5,300) # appel a la fonction flocon avec n = 5 et cote = 300

""" Fonction faites avec GPT 3.5"""
def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)

koch_snowflake(franklin, 5, 300) # appel a la fonction koch_snowflake avec n = 5 et cote = 300

def draw_koch_snowflake():
    screen = Screen()
    
    screen.bgcolor("white")
    franklin.shape("turtle")
    franklin.color("blue")
    franklin.speed(2)

    franklin.penup()
    franklin.goto(-150, 50)
    franklin.pendown()

    # Dessiner les deux premières étapes du flocon de Koch
    for _ in range(3):
        von_koch(2, 300)
        franklin.right(120)

    screen.exitonclick()

# Appeler la fonction pour dessiner le flocon de Koch
#draw_koch_snowflake()
exitonclick()