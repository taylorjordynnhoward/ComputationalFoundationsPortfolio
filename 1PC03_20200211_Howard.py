#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#========
#PC03- Generative Art
#Howard
#DATE(20201102)
#
#This code is designed to create loops
#========
from random import * 
from turtle import *
money = Screen()
money.clear()
money.bgcolor("white")

moves = 10 #variable for range
big = 5 #variable for turtle size
#two variables I created

sebastian = Turtle(visible=False)
sebastian.width(big)
sebastian.color("pink")
sebastian.speed("fastest")

#pink star
for num in range(moves):
    sebastian.forward(70)
    sebastian.left(150)
     #used a loop   
    
#blue star
rafael = Turtle()
rafael.width(big)
rafael.color(222/255,197/255,227/255)
rafael.speed("fastest")
rafael.goto(-150,100)

for num in range(moves):
        rafael.forward(80)
        rafael.left(160)
        #second loop

#purple star
indigo = Turtle(visible=False)
indigo.color(205/255,237/255,253/255)
indigo.speed("fastest")
indigo.width(big)


x = randint(-300,300)
y = randint(-300,300)
indigo.goto(x,y)
indigo.down()
   #used randint to make indigo turtle show up different, random places
for i in range (moves):
    indigo.forward(80)
    indigo.left(160)

#green star
court = Turtle(visible=False)
court.color(160/255,232/255,175/255)
court.speed("fastest")
court.width(big)

x = randint(-300,300)
y = randint(-300,300)
court.goto(x,y)
court.down()
   #used randint to make indigo turtle show up different, random places
for i in range (moves):
    court.forward(80)
    court.left(160)
    
#green star
cat = Turtle(visible=False)
cat.color(232/255,255/255,183/255)
cat.speed("fastest")
cat.width(big)

x = randint(-300,300)
y = randint(-300,300)
cat.goto(x,y)
cat.down()
   #used randint to make indigo turtle show up different, random places
for i in range (moves):
    cat.forward(80)
    cat.left(160)
