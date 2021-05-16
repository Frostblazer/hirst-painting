# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 10)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle

import random

from turtle import Turtle, Screen

turtle_object = Turtle()

color_list = [(235, 234, 231), (236, 230, 233), (232, 240, 235), (225, 233, 238), (237, 34, 109), (153, 24, 65),
              (240, 73, 34), (7, 147, 92), (218, 170, 46), (178, 159, 44)]

turtle.colormode(255)

turtle_object.penup()
turtle_object.hideturtle()

y = -200

while y < 250:

    turtle_object.setx(-200)
    turtle_object.sety(y)

    for dot in range(10):
        turtle_object.dot(20, color_list[random.randint(0,9)])
        turtle_object.forward(50)

    y = y + 50


screen_object = Screen()
screen_object.exitonclick()