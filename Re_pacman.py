"""Rerpoduce the results of the code:pacman.py"""
from random import choice
from turtle import *
from freegames import floor,vector

state = {'score':0}
"""Game state dictionary,record score"""
path = Turtle(visible=False)
"""Create two invisible turtle objects,one for drawing the path and one for displaying the score"""
writer = Turtle(visible=False)
aim = vector(5,0)
""" Define the direction of the pacman,initially to the right"""
pacman = vector(-20,-80)
"""Define the initial position of the pacman"""
ghosts = [
    [vector(-180,160),vector(10,0)],
    [vector(-180,-160),vector(0,10)],
    [vector(100,160),vector(0,-10)],
    [vector(100,-160),vector(-10,0)],
]
"""Define the initial position and direction of the ghosts"""
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
"""Define the layout of the map,0 represnts the wall,1 represents the path"""
def square(x,y):
    """Draw square using path at (x,y)"""
    path.up()
    path.goto(x,y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    """Return index in tiles for pacman."""
    x = (floor(point.x,20)+200)/20
    y = (180-floor(point.y,20))/20
    index = int(x + y*20)
    return index

def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False
    index = offset(point + 19)

    if tiles[index] == 0:
        return False
    
    return point.x % 20 == 0 or point.y %20 == 0

def change(x,y):
    """Change the direction of the pacman"""
    if valid(pacman + vector(x,y)):
        aim.x = x
        aim.y = y

def world():
    """Draw world using path."""
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x,y)

            if tile == 1:
                path.up()
                path.goto(x+10,y+10)
                path.dot(2,'white')

def distance_close(pacman,ghost):
    """Return True if pacman is too close to ghost"""
    if abs(pacman.x - ghost.x) <200 and abs(pacman.y - ghost.y) < 200:
        return True
    return False

def move():
    """Move pacman and ghosts"""
    writer.undo()
    writer.write(state['score'])
    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x,y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20,'yellow')

    for point,course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5,0),
                vector(-5,0),
                vector(0,5),
                vector(0,-5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y
        
        up()
        goto(point.x + 10, point.y + 10)
        dot(20,'red')
        
        ghost_speed = 100
        
        if distance_close(pacman,point):
            ghost_speed = 30
    
    update()
    
    """A game-over condition"""
    for point,course in ghosts:
        if abs(pacman - point) < 20:
            return
    
    ontimer(move,ghost_speed)

"""Main function"""
setup(420,420,370,0)
"""Set up the window size and position"""
"""It has four parameters,represent width,height,x,y"""
hideturtle()
"""Hide the turtle"""
tracer(False)
"""Disable animation"""
writer.goto(160,160)
"""Move the writer turtle to the top right corner of the screen"""
writer.color('white')
"""Set the color of the writer turtle to white"""
writer.write(state['score'])
"""Write the initial score"""
listen()
"""Listen for keyboard events to control the pacman"""
onkey(lambda: change(5,0),'Right')
"""Change the direction using the function change"""
onkey(lambda: change(-5,0),'Left')
onkey(lambda: change(0,5),'Up')
onkey(lambda: change(0,-5),'Down')
world()
"""Draw the map"""
move()
"""Start the game loop"""
done()
"""End the game loop and keep the window open"""