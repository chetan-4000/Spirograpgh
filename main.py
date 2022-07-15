from turtle import Turtle,Screen
import random

timmy = Turtle()
timmy.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]

def shapes(sides):
    sides = 5
    angle = 360/sides
    for i in range(sides):
        timmy.forward(100)
        timmy.left(angle)
def Random_Walk():
    for i in range(200):
        timmy.forward(25)
        timmy.pensize(10)
        timmy.setheading(random.choice(directions))
        timmy.color(random.choice(colours))
def Drawing_Spirograph(size_of_gap):
    timmy.speed("fastest")
    for i in range(int(360/size_of_gap)):
        timmy.color(random.choice(colours))
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

Drawing_Spirograph(10)





screen = Screen()
screen.exitonclick()