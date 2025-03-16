# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:06:52 2024

@author: varun
"""
import random

# =============================================================================
# from prettytable import PrettyTable
# table = PrettyTable()
# 
# table.add_column("Pokémon Name",["Pikachu" ,"Squirtle", "Charmander"])
# table.add_column("Type" , ["Electric" , "Water", "Fire"])
# print (table)
# c=(2,3,4)
# print (c)
# =============================================================================
import turtle as t

t.colormode(255)
tim = t.Turtle()
shapes_A = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
direction = [0,90,180,270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
screenProp=t.Screen()
tim.pensize(4)
t.colormode(225)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color_tuple = (r,g,b)
    return(color_tuple)

def forward():
    tim.forward(3)
def backward():
    tim.backward(10)
def clockwise():
    new_heading =tim.heading()+10
    tim.setheading(new_heading)
def anti_clockwise():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)
def clockwise_circle():
    tim.circle(60,30)
def clear():
    tim.reset()
    
    
screenProp.listen()
screenProp.onkeypress(key = "Up", fun=forward)
screenProp.onkeypress(key = "Down", fun=backward)
screenProp.onkeypress(key = "Left", fun=anti_clockwise)
screenProp.onkeypress(key = "Right", fun=clockwise)
screenProp.onkeypress(key = "c", fun=clear)


    
    



# ============================== Drawimg Dots ===============================================
# d=10
# tim.home()
# xpos=-250.0
# ypos=-250.0
# tim.teleport(xpos, ypos)
# tim.setpos(xpos, ypos)
# print(screenProp.canvwidth)
# tim.hideturtle()   
# row=0
# tim.penup()
# while row < 10:
#     tim.teleport(xpos, ypos)
#     for _ in range (10):
#        print(tim.position())
#        tim.color(random_color())
#        tim.dot(20)
#        tim.fd(50)
#        
#     ypos+=50
#     row+=1    
# 
# =============================================================================
   
   


# =================== Shanpes pattern 3 to 10==========================================================
# def draw_shape_Right(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(50)
#         tim.right(angle)
# def draw_shape_Left(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(50)
#         tim.left(angle)        
# 
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape_Right(shape_side_n)
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape_Left(shape_side_n)   
#     
# =============================================================================
# =================================Random Move============================================
# def randon_move():
#     tim.forward(20)
#     tim.left(random.choice(direction))
# tim.speed(10)    
# for move in range(1,100):
#     
#     tim.shape(random.choice(shapes_A))
#     tim.color(random_color())
#     randon_move()
#     
# =============================================================================

# ============================== Circle design ===============================================
# def pattern_circle():
#      tim.circle(80)
#      tim.left(10)
#      
# tim.speed(0) 
# 
# for move in range(1,100): 
#      tim.shape(random.choice(shapes_A))
#      tim.color(random_color())
#      tim.begin_fill()
#      pattern_circle()
#      tim.end_fill()
# tim.circle(80,0.4,3)
# =============================================================================

screenProp.exitonclick()    
