from myFunction import *
import turtle

rose = turtle.Turtle()
bob = turtle.Turtle()
turtle.colormode(255)
bob.speed(0)
rose.speed(0)
turtle.bgcolor("black")

#OmbreTriangleSpiral
for times in range(256):
    bob.begin_fill()
    c = (times,120,145)
    bob.color(c)
    polygon(bob,3,50)
    bob.left(50)
    bob.forward(times)
    bob.end_fill()

#LinesCrossingInMiddleMakingItAccidentlyLookLikeAFerrisWheel
for times in range(15):
    bob.width(2)
    c = (0,0,0)
    bob.color(c)
    jump(bob,0,0)
    bob.left(90)
    L(bob,500,175)
    
#BlackTriangleInCenter
rose.right(120)
rose.begin_fill()
for times in range(3):
    rose.forward(600)
    rose.left(120)
rose.end_fill()

#WhiteTriangleOutlineInCenter
jump(rose,0,-50)
rose.pencolor("white")
rose.begin_fill()
for times in range(3):
    rose.forward(400)
    rose.left(120)
rose.end_fill()

#WhiteTearSpiralCloudThings
for times in range(11):
    bob.width(1)
    c = (255,255,255)
    bob.color(c)
    jump(bob,-300,300)
    tear(bob)
    rose.color(c)
    jump(rose,300,300)
    tear(rose)



