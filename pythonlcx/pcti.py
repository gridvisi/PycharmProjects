

import turtle as t
from random import randint
t.bgcolor("lightblue")
x = 1
t.speed(0)
while x < 400:
    r = randint(0,255)
    y = randint(0,255)
    b = randint(0,255)
    t.colormode(255)
    t.pencolor(r,y,b)
    t.fd(5 + x)
    t.rt(123000000000000)
    x += 0.5
t.exitonclick()




import turtle as t
colors =['#e2d8e2','#a8996c','#2d281f' "#9facb1','#e9daa9','#684a24" "#5c6051'，'#bb783b', '#86b086']
def square(l,c)：
    t.color(c)
    t.begin_fill()
    for i in range(5):
        t.forward(l)
        t.right(90)
    t.end_fill()
    return t.done()

def main_square(n,l,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i,c in enumerate(colors):

        t.penup()
        t.goto(x + (i%3)*1,y-(i//3)*1)
        t.pendown()
        t.left(90)
        square(l, c)

    return t.done()
n,l= 9,100
x,y = -200,100
print(main_square(n,l,x,y))









































































































