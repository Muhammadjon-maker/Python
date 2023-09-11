import os
import math
os.system("cls")

list = [
    "Vivian Kidd", "Bradyn Grant", "Alexis Strickland", "Madeleine Dunn",
    "Emanuel Deleon", "Charlotte Moody", "Ian Wells", "Greyson Sellers",
    "Abril Cordova", "Julissa Wolf", "Gabrielle Osborne", "Brian Webster",
    "Ethen Charles", "Ashtyn Cowan", "Brycen Benson", "Thomas Sexton",
    "Brynlee Park", "Keaton Pena", "Lily Ochoa", "Jaycee Glass",
    "Anderson Stark", "Alexandria Harper", "Derek Cooley", "Savannah Coleman",
    "Chase Cantu", "Maverick Gonzales", "Wyatt Browning", "Brenden Walter",
    "Paula Bullock", "Alisha Hicks", "Genevieve Petty", "Reece Erickson",
    "Brice Pope", "Maverick Hammond", "Giuliana Morris", "Kaelyn Kelley",
    "Paisley French", "Cassius Rogers", "Gloria French", "Hugh Richardson",
    "Braiden Tate", "Sophia Wang", "Cortez Kirby", "Sebastian Wilkinson",
    "Joanna Shannon", "Miracle Barrera", "Cali Kaiser", "Bridget Leon",
    "Gillian Hall", "Jade King", "Aydin Powell", "Anthony Paul",
    "Brittany Rios", "Arely Howe", "Trace Valenzuela", "Aryanna Hicks",
    "Connor Nixon", "Santiago Vargas", "Kirsten Monroe", "Norah Schultz",
    "Danika Hudson", "Makena Escobar", "Jayce Navarro", "Thaddeus Strickland",
    "Michaela Robinson", "Remington Hurley", "Jairo Sanders", "Averie Huber",
    "Cody Jensen", "Kennedy Wall", "Fiona Huynh", "August Tapia",
    "Sarah Manning", "Joselyn Allison", "Dayton Barnes", "Santiago Glenn",
    "Rashad Cuevas", "Bernard Nicholson", "Will Moyer", "Aliza Frazier",
    "Abram Burch", "Lilly Klein", "Carlee Montes", "Madeleine Patton",
    "Brady Osborn", "Ruth Monroe", "Celia Horn", "Braylen Cabrera",
    "Jennifer Tanner", "Kendra Cross", "Olive Sherman", "Aiyana Wolfe",
    "Charlize Cervantes", "Braydon Esparza", "Kash Osborne", "Maximus Mathews",
    "Kamora Richardson", "Tripp Sosa", "Kameron Taylor", "Tyler Jackson"
]

list.sort()

for ism in list:
    print(ism)

# import turtle
# # import colorsys
# # t= turtle.Turtle()
# # s = turtle.Screen().bgcolor('black')
# # t.speed(0)
# # n=70
# # h=0
# # for i in range(360):
# #  c= colorsys.hsv_to_rgb(h, 1, 0.8)
# #  h+= 1/n
# #  t.color(c)
# #  t.left(1)
# #  t.fd(1)
# #  for j in range(2):
# #   t.left(2)
# #   t.circle(100)

# # from turtle import *
# # import colorsys
# # bgcolor('black')
# # tracer(10)
# # pensize(5)
# # h = 0
# # for i in range(300):
# #     c = colorsys.hsv_to_rgb(h, 1, 1)
# #     h += 0.005
# #     pencolor(c)
# #     fillcolor('black')
# #     begin_fill()
# #     for j in range(2):
# #         fd(i * 1.2)
# #         rt(60)
# #         fd(300)
# #         rt(120)
# #     rt(121)
# #     end_fill()
# # done()

# # import turtle
# import turtle
 
# # defining colors
# colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']
 
# # setup turtle pen
# t= turtle.Pen()
 
# # changes the speed of the turtle
# t.speed(10)
 
# # changes the background color
# turtle.bgcolor("black")
 
# # make spiral_web
# for x in range(200):
#     t.pencolor(colors[x%6]) # setting color
#     t.width(x/100 + 1) # setting width
#     t.forward(x) # moving forward
#     t.left(59) # moving left
 
# turtle.done()
# t.speed(10)
 
# turtle.bgcolor("black") # changes the background color
 
# # make spiral_web
# for x in range(200):
#     t.pencolor(colors[x%6]) # setting color
#     t.width(x/100 + 1) # setting width
#     t.forward(x) # moving forward
#     t.left(59) # moving left
 
# turtle.done()