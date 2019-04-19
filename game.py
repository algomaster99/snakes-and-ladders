#-------------------------------------------------------------------------------
# Name:        Snakes & Ladders
# Purpose:     Computer Science Project
#
# Author:      Aman Sharma
#
# Created:     06-02-2016
# Copyright:   Aman Sharma
# Licence:
#-------------------------------------------------------------------------------

#Playing Board------------------------------------------------------------------
from turtle import *
hideturtle()
penup()
speed(10)
screensize(600,600)
goto(0,275)
write("Welcome to Snakes & Ladders 2.0",align="center",font=("Times New Roman",22,"bold"))

"""--------------------------Instructions------------------------------------"""
goto(-650,250)
write("Instructions:-",font=("arial",18,"underline"))
instructions=["1. Snakes & Ladders are marked with different colours.","2. If you get 3 sixes in a row, your turn \
will be cancelled.","3. Player who is first to reach 100, wins the game.","4. Red is Player 1, Blue is Computer 1 &"]
a=-650
b=200
for j in instructions:
    goto(a,b)
    write(j,font=("arial",12,"normal"))
    b-=75
goto(-650,-50)
write("Green is Computer 2",font=("arial",12))
goto(-650,-100)
write("Don't play it during your exams,",font=("arial",12))
goto(-650,-125)
write("You might get addicted! ;)",font=("arial",12))
pendown()
"""--------------------------------------------------------------------------"""

"""----------------------Co-ordinate Converter-------------------------------"""
def coordinate_converter(start,y):
    d={}
    a=start
    for x in range(-225,226,50):
        d[a]=[x,y]
        if start%2<>0:
            a+=1
        else:
            a-=1
    return d
d1=coordinate_converter(1,-275)
d2=coordinate_converter(20,-225)
d3=coordinate_converter(21,-175)
d4=coordinate_converter(40,-125)
d5=coordinate_converter(41,-75)
d6=coordinate_converter(60,-25)
d7=coordinate_converter(61,25)
d8=coordinate_converter(80,75)
d9=coordinate_converter(81,125)
d10=coordinate_converter(100,175)
d={}
for dictionary in [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]:
    d.update(dictionary)
"""--------------------------------------------------------------------------"""

"""----------------Filling the Boards(Numbering & Colouring)-----------------"""
def numbering(value):
    l1=d.values()
    index=l1.index(value)
    l2=d.keys()
    return str(l2[index])
def board(a,b,color="",text="",size=50):
    width(3)
    penup()
    goto(a,b)
    pendown()
    fillcolor(color)
    begin_fill()
    for i in range(4):
        fd(size)
        rt(90)
    end_fill()
    penup()
    fd(10)
    write(text,font=("Arial",8,"bold"))

start_x=-250
start_y=-250
snakes={99:[125,-225],72:[225,-75],45:[-75,-225],85:[25,-25],62:[75,-175]}
ladders={20:[225,25],42:[225,175],12:[75,-75],67:[-75,125]}
for y in range(start_x,250,50):
    for x in range(start_y,250,50):
        if (x==-200 and y==200):
            board(x,y,"dark slate gray",text="Snake")
        elif x==150 and y==100:
            board(x,y,"yellow",text="Snake")
        elif x==-50 and y==-50:
            board(x,y,"Lime Green",text="Snake")
        elif x==-50 and y==150:
            board(x,y,"pink",text="Snake")
        elif x==-200 and y==50:
            board(x,y,"orange",text="Snake")
        elif x==100 and y==-200:
            board(x,y,"dark slate gray",text="|:(|")
        elif x==200 and y==-50:
            board(x,y,"yellow",text="|:(|")
        elif x==-100 and y==-200:
            board(x,y,"Lime Green",text="|:(|")
        elif x==0 and y==0:
            board(x,y,"pink",text="|:(|")
        elif x==50 and y==-150:
            board(x,y,"orange",text="|:(|")
        elif x==-250 and y==-200:
            board(x,y,"lightsalmon",text="Ladder")
        elif x==200 and y==50:
            board(x,y,"lightsalmon",text="|:)|")
        elif x==-200 and y==-50:
            board(x,y,"firebrick",text="Ladder")
        elif x==200 and y==200:
            board(x,y,"firebrick",text="|:)|")
        elif x==150 and y==-200:
            board(x,y,"purple",text="Ladder")
        elif x==50 and y==-50:
            board(x,y,"purple",text="|:)|")
        elif x==50 and y==50:
            board(x,y,"dark khaki",text="Ladder")
        elif x==-100 and y==150:
            board(x,y,"dark khaki",text="|:)|")
        else:
            board(x,y)
for k in d.values():
    penup()
    goto(k[0],k[1])
    write(numbering(k))
"""--------------------------------------------------------------------------"""
#-------------------------------------------------------------------------------
def dice_roll_display(posx,posy):
    board(posx,posy,color="white",size=120)
    penup()
    goto(posx+5,posy-20)
    write("Player 1:",font=("arial",12))
    goto(posx+5,posy-60)
    write("Computer 1:",font=("arial",12))
    goto(posx+5,posy-100)
    write("Computer 2:",font=("arial",12))

def snakeladder_display(posx,posy):
    board(posx,posy,color="white",size=155)

def information(posx,posy,word,size):
    goto(posx,posy)
    write(word,font=("Times New Roman",size,"bold"))

#Defining Pawns-----------------------------------------------------------------
pencolor("black")
speed(0)
initial=Turtle()
player1=initial.clone()
player1.penup()
player1.fillcolor("red")
player1.shape("circle")
player1.goto(-260,-257)
player1.speed(1)
pc1=initial.clone()
pc1.penup()
pc1.fillcolor("blue")
pc1.shape("circle")
pc1.goto(-260,-275)
pc1.speed(1)
pc2=initial.clone()
pc2.penup()
pc2.fillcolor("green")
pc2.shape("circle")
pc2.goto(-260,-293)
pc2.speed(1)
initial.ht()
#-------------------------------------------------------------------------------

import random
def choice():
    ask=raw_input("Press 'Enter' for Roll or 'Q' to Quit")
    return ask

#Dice Roll----------------------------------------------------------------------
def dice():
    l=[]
    chance=0
    num=random.randrange(1,7)
    l.append(num)
    if num==6:
        num1=random.randrange(1,7)
        l.append(num1)
        if num1==6:
            num2=random.randrange(1,7)
            l.append(num2)
            return l
        else:
            return l
    else:
        return l

def dice_returner(lst):
    chance=0
    for i in lst:
        chance=chance+i
    if chance==18:
        return 18
    else:
        return chance
#-------------------------------------------------------------------------------

#Movement of Pawns--------------------------------------------------------------
def x_cor_returner(d,numonboard):
    l1=d.keys()
    num=l1.index(numonboard)
    l2=d.values()
    x_cor=l2[num][0]
    return x_cor
def y_cor_returner(d,numonboard):
    l1=d.keys()
    num=l1.index(numonboard)
    l2=d.values()
    y_cor=l2[num][1]
    return y_cor
def snakeladder(l,numonboard,name_turtle):
    l1=l.keys()
    num=l1.index(numonboard)
    l2=l.values()
    x_cor=l2[num][0]
    y_cor=l2[num][1]
    name_turtle.goto(x_cor,y_cor)
    newstart=[]
    newstart.append(x_cor)
    newstart.append(y_cor)
    return newstart
def aftereffect(lst,dct):
    l1=dct.values()
    number=l1.index(lst)
    l2=dct.keys()
    final=l2[number]
    return final
#-------------------------------------------------------------------------------

#The Game-----------------------------------------------------------------------
start1=0
start2=0
start3=0
while start1<>100 or start2<>100 or start3<>100:
    chance=0
    perm=choice()
    dice_roll_display(360,-5)
    snakeladder_display(350,-180)
    speed(10)
    if perm=="":
        num=dice_returner(dice())
        information(460,-25,str(num),12)
        print "Player1:",num
        if num==18:
            start1=start1
        elif num<6 and start1==0:
            start1=start1
        elif start1==0 and num>6 and num<>18:
            start1=start1+(num-6)
            player1.goto(x_cor_returner(d,start1),y_cor_returner(d,start1))
            information(350,120,"Player 1 is aboard.",15)
        elif start1+num==100:
            information(-650,-200,"Player 1 Wins!",15)
            player1.goto(x_cor_returner(d,start1+num),y_cor_returner(d,start1+num))
            break
        elif start1+num>100:
            start1=start1
        elif start1+num<100:
            start1=start1+num
            if start1 in snakes:
                player1.goto(x_cor_returner(d,start1),y_cor_returner(d,start1))
                information(360,-200,"You were bitten",12)
                information(360,-212,"by a snake!",12)
                print "You were bitten by a snake!"
                l=snakeladder(snakes,start1,player1)
                start1=aftereffect(l,d)
            elif start1 in ladders:
                player1.goto(x_cor_returner(d,start1),y_cor_returner(d,start1))
                information(360,-200,"You climbed",12)
                information(360,-212,"a ladder!",12)
                print "You climbed a ladder!"
                l=snakeladder(ladders,start1,player1)
                start1=aftereffect(l,d)
            else:
                player1.goto(x_cor_returner(d,start1),y_cor_returner(d,start1))

    elif perm=="Q":
        break
    else:
        print "Invalid Input"

    #Computer 1's Turn
    if perm=="":
        num=dice_returner(dice())
        information(460,-65,str(num),12)
        print "Computer 1:",num
        if num==18:
            start2=start2
        elif num<6 and start2==0:
            start2=start2
        elif start2==0 and num>6 and num<>18:
            start2=start2+(num-6)
            pc1.goto(x_cor_returner(d,start2),y_cor_returner(d,start2))
            information(350,70,"Computer 1 is aboard.",15)
        elif start2+num==100:
            information(-650,-200,"Computer 1 Wins!",15)
            pc1.goto(x_cor_returner(d,start2+num),y_cor_returner(d,start2+num))
            break
        elif start2+num>100:
            start2=start2
        elif start2+num<100:
            start2=start2+num
            if start2 in snakes:
                pc1.goto(x_cor_returner(d,start2),y_cor_returner(d,start2))
                information(360,-245,"Computer 1 was bitten",12)
                information(360,-257,"by a snake!",12)
                print "Computer 1 was bitten by a snake!"
                l=snakeladder(snakes,start2,pc1)
                start2=aftereffect(l,d)
            elif start2 in ladders:
                pc1.goto(x_cor_returner(d,start2),y_cor_returner(d,start2))
                information(360,-245,"Computer 1 climbed",12)
                information(360,-257,"a ladder!",12)
                print"Computer 1 climbed a ladder!"
                l=snakeladder(ladders,start2,pc1)
                start2=aftereffect(l,d)
            else:
                pc1.goto(x_cor_returner(d,start2),y_cor_returner(d,start2))
    else:
        continue

    #Computer 2's Turn
    if perm=="":
        num=dice_returner(dice())
        information(460,-105,str(num),12)
        print "Computer 2:",num
        if num==18:
            start3=start3
        elif num<6 and start3==0:
            start3=start3
        elif start3==0 and num>6 and num<>18:
            start3=start3+(num-6)
            pc2.goto(x_cor_returner(d,start3),y_cor_returner(d,start3))
            information(350,20,"Computer 2 is aboard.",15)
        elif start3+num==100:
            information(-650,-200,"Computer 2 Wins!",15)
            pc2.goto(x_cor_returner(d,start3+num),y_cor_returner(d,start3+num))
            break
        elif start3+num>100:
            start3=start3
        elif start3+num<100:
            start3=start3+num
            if start3 in snakes:
                pc2.goto(x_cor_returner(d,start3),y_cor_returner(d,start3))
                information(360,-290,"Computer 3 was bitten",12)
                information(360,-302,"by a snake!",12)
                print "Computer 2 was bitten by a snake!"
                l=snakeladder(snakes,start3,pc2)
                start3=aftereffect(l,d)
            elif start3 in ladders:
                pc2.goto(x_cor_returner(d,start3),y_cor_returner(d,start3))
                information(360,-290,"Computer 3 climbed",12)
                information(360,-302,"a ladder!",12)
                print"Computer 2 climbed a ladder!"
                l=snakeladder(ladders,start3,pc2)
                start3=aftereffect(l,d)
            else:
                pc2.goto(x_cor_returner(d,start3),y_cor_returner(d,start3))
    else:
        continue
#-----------------------------End of Program-----------------------------------#

