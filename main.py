###############
#  My solution
###############

import colorgram
import random
from turtle import Turtle, Screen
import turtle

six_objects=colorgram.extract('hirst-spots-image.jpg',30)

rgb_tuple_list=[]
for each in six_objects:
	rgb=each.rgb
	new_tuple=(rgb[0],rgb[1],rgb[2])
	rgb_tuple_list.append(new_tuple)
print(rgb_tuple_list)
tim = Turtle()
turtle.colormode(255)


tim.penup()
tim.hideturtle()
tim.setpos(-25,25)
for x in range (10):
		print(tim.position())
		for y in range (10):
			rand_color=random.choice(rgb_tuple_list)
			print(rand_color)
			tim.dot(20,rand_color)
			tim.penup()
			tim.forward(50)
		x +=1
		tim.setpos(-25.00,(x*50)+25)
		print(f" X is : {x}")
	

screen = Screen()
screen.exitonclick()

###############
# instructor's solution in main2.py
###############

