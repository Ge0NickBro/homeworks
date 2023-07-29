from turtle import *


#we want to paint a house

#step 1: draw a square
#speed(70) #change speed by ur choice
width(7)
color("purple")
forward(200)
left(90)
                

forward(200)
left(90)



forward(200)
left(90)
forward(200)
left(90)
#end of square

#start of door


forward(70)
color("yellow")
left(90)

forward(120)
right(90)

forward(60)
right(90)

forward(120)
#end of door

#start of roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()
#end of roof
#start of windows
penup()
goto(0, 0)


width(4)
color("cyan")
goto(15, 90)
pendown()

left(120)
forward(40)

left(90)
forward(50)

left(90)
forward(40)

left(90)
forward(50)

left(90)
forward(20)

left(90)
forward(50)

left(90)
forward(20)

left(90)
forward(25)

left(90)
forward(40)



#end of house

# #start of background
penup()
goto(-1, 0)
pendown()
color("green")

width(18)

left(180)
forward(350)

right(180)
forward(700)

exitonclick()