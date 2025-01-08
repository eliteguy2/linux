"""
# Cookie Clicker game

# You will also need a gif in the same folder, below is the cookie gif link:

# https://vle.newcollege.ac.uk/mod/resource/view.php?id=1551354


import turtle



wn = turtle.Screen()

wn.title("cookie clicker")

wn.bgcolor("black")



wn.register_shape(r"C:\Users\noron\Documents\joshua homework\cookie2\cookie.gif.gif")



cookie = turtle.Turtle()

cookie.shape(r"C:\Users\noron\Documents\joshua homework\cookie2\cookie.gif.gif")

cookie.speed(0)



clicks = 0



pen = turtle.Turtle()

pen.hideturtle()

pen.color("white")

pen.penup()

pen.goto(300, 400)

pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))



def clicked(x, y):
        global clicks
        clicks += 1
        pen.clear()
        pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

cookie.onclick(clicked)



wn.mainloop()
"""
# More advanced Cookie Clicker , changing backcolour and image when clicked enough times



import turtle

from random import uniform

wn = turtle.Screen()

wn.title("Cookie Clicker")

wn.bgcolor("green")



wn.register_shape(r"C:\Users\noron\Documents\joshua homework\cookie2\cookie.gif.gif")



cookie = turtle.Turtle()

cookie.shape(r"C:\Users\noron\Documents\joshua homework\cookie2\cookie.gif.gif")

cookie.speed(0)



clicks = 0



pen = turtle.Turtle()

pen.hideturtle()

pen.color("white")

pen.penup()

pen.goto(200, 200)

pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))





def clicked(x, y):

    global clicks

    clicks += 1

    pen.clear()

    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

    if clicks >5:

        wn.bgcolor("red")



    if clicks > 10:

        wn.bgcolor("black")

        wn.register_shape(r"C:\Users\noron\Documents\joshua homework\cookie2\cookie.gif.gif")

        cookie = turtle.Turtle()

        cookie.shape(r"C:\Users\noron\Documents\joshua homework\cookie2\cookie.gif.gif")

        cookie.speed(0)

        pen.goto(0, 0)

        pen.color("black")

        pen.write(f"Game over", align="center", font=("Courier New", 32, "normal"))

        



#if called this function will move the cookie around

def movement():

    turtle.shape(r"C:\Users\noron\Documents\joshua homework\cookie2\cookie.gif.gif")

    turtle.speed(10)

    for i in range (1,100):

        #random angle 

        a = uniform(-90,90)

        turtle.left(a)

        #random move

        d = uniform(-100,100)

        turtle.forward(d)

  

   

cookie.onclick(clicked)



wn.mainloop()


