from  turtle import*
#To hide a turtle use this command.
hideturtle()
 
#it is used to fill the color.

fillcolor('red')

begin_fill()

#for is used with range
for i in [300, 200] *2:
     forward(i)
     circle(30, 90)
#here by using some commands the turtle moves accordingly.
end_fill()
penup()
goto(120, 80)
pendown()
fillcolor('white')
begin_fill()
for i in [30, 120, 120]:
    left(i)
    forward(100)
end_fill()
done
