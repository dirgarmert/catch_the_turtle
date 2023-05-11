import random
import turtle
import time

kaplumbaga_screen = turtle.Screen()
kaplumbaga_screen.title("Kaplumbaga Turtle")
kaplumbaga_screen.screensize(canvwidth=400, canvheight=400,
                             bg="light Blue")
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("green")
kaplumbaga.penup()

while True:
    kaplumbaga.forward(50)
    kaplumbaga.right(random.randint(0, 360))
    kaplumbaga.penup()
    time.sleep(3)

turtle.mainloop()
