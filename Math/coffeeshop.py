# https://brilliant.org/daily-problems/taxicab-distance-5/

def distEqual(home,location):  #coordinate
    short = float('inf')
    x,y = home
    for i,j in location:
        s = x-i + y-j
        if s < short:
            tag = (i,j)
            #tag = [i,j]
            short = s
    return tag

location = [(-4,3),(-1,-1),(2,-4)]
home = (3,4)
print(distEqual(home,location))

# upgrade coffeeshop
# every shop target users not exceed distance 5 min,
# so that how many cross cover

#coordinate X,Y
import turtle as t
def xy():

    t.pensize(5)
    t.color("black")
    t.goto(-300,0)
    t.pendown()
    t.forward(600)
    t.penup()
    t.goto(0,300)
    t.pendown()
    t.right(90)
    t.forward(600)
    #t.done()

#print(xy())

# grid
def grid(start,end,ratio):
    t.goto(0,0)
    t.dot(8,'red')
    for y in range(start[1],end[1],-1):
        for x in range(start[0], end[0]):
            #x,y = xy
            t.penup()
            t.goto(x*ratio,y*ratio)
            t.pendown()
            t.dot(10,'green')
    t.done()
    #return t.done
start,end,ratio = (-3,3),(3,-3),90
print(grid(start,end,ratio))



def capicity(time,zero):

    x,y = zero
    loc = []
    for x in range(-time+x,x+time+1):
        #print(x)
        loc.extend([(x,time-abs(x)),(x,abs(x)-time)])
    return set(loc)  #len(set(loc)),
time = 5
zero = (-1,0)
#print(capicity(time,zero))

'''

pos = capicity(time,zero)
ratio=40
xy()
for xy in pos:
    x, y = xy
    t.dot(10,'green')
    t.penup()
    t.goto(x * ratio, y * ratio)
    t.pendown()
    t.dot(10, 'red')
#t.done()


'''
