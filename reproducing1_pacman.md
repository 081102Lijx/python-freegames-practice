As the first project in my GitHub, I want to make something interesting but not too difficult. It's not alien for me to comprehend and thumb through such games in python, but it is the absolutely first time to reproduce a total-functioned code. I will write down what I'm thinking and how I  deconstruct  classical projects to do my utmost to enhance my comprehension about coding.

## Dependencies

We leverage the following core libraries for system implementation:

- **random** (choice,to choose an element from a non-empty sequence,such as list,tuple or string )
- **turtle** (mainly used for drawing and creating simple graphical user interfaces)

## Global  Variations

This section outlines the global variables used throughout the project,their purpose,and how they can be utilized.

- **state = {'score':0}** : it's used to record scores as a game stats dictionary

- **path = Turtle(visible=False** : create an  invisible turtle objects for drawing the path

- **writer = Turtle(visible=False)** : create an invisible turtle objects for displaying the score

- **aim = vector(5,0)** : define the moving direction of Pac-man, initially set to the right

- **pacman = vector(-40,-80)** : define the initial position of Pac-man

- **ghosts = [
      [vector(-180, 160), vector(5, 0)],
      [vector(-180, -160), vector(0, 5)],
      [vector(100, 160), vector(0, -5)],
      [vector(100, -160), vector(-5, 0)],
  ]** : define the initial position and moving direction of ghosts

- **tiles = [0,0,1,0 ...]** : define layout of map.0 for walls, 1 for available paths

  

## Running Logic

This section details the running logic of the game, converting the progress of a running circle,explaining functions of several core  code.

```python
setup(420,420,370,0)
```

It's used to setup size and position of game window.

```python
hideturtle()
tracer(False)
```

I put these line together for the same purpose: to make the game window clean and tidy. Let's explain it more tangibly.

**hideturtle**:  hide the censor of the turtle (usually an arrow shape), which is redundant in games because we only need to draw the map and characters,to improve visual effects and make the game interface cleaner.

**tracer(False)**: by default, the turtle draws each line or shape step by step,which can be quite slow when drawing complex graphics. After turning off the animation, all drawing operations will be completed immediately, improving the drawing speed. As games requiring real-time screen updates and frame-by-frame drawing causing noticeable delays, it's wiser to turn off the animation to update the game screen more smoothly.

```python
writer.goto(160,160)
writer.color('white')
writer.write(state['score'])
```

These are initial UI set for scores, to show the real-time score of player.

**writer.goto**: it's used to put an invisible turtle element wirter to a certain position

**writer.color & writer.write**: to paint the invisible turtle element as 'score' in white

All in all, these three sentences are used to set the score's position, color and content.

```python
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
```

They are used to control the movement of Pac-man through keyboard input. From the function **change()**, when users push "right", the Pac-man will move towards right for a unit, by the same token the user can use keyboard to control the Pac-man's movement.

```python
world()
move()
done()
```

These are key functions to run the game. **world()** is for drawing the map in the game, **move()** is the core function which control the movement of Pac-man and ghost and the running logic in ending or winning, I will explain it later,**done()** is used to end up the game after **move()** ends.

This is the running logic of Pac-man, after these functions, we can build an easy Pac-man game in python. But it's not for all, now, we steal have several questions.

- How to realize functions such as **change(), world(),move()**, what about their input and output?
- How to define *food*  in this game?

Let's solve them in the next part.

## Functions

This section lists the main functions available in the projects along with their **descriptions**, **parameters** and **usage examples**.

### 1.change()

**descriptions:** it's used to change the movement of the Pac-man.

**parameters:** x, y

**usage example:** line third and forth represent for the assignment of x, y in aim.

```python
def change(x, y):
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y
```

It will appear in the running logic, after main function listening to the keyboard and want to move the Pac-man, called for the certain function to move the Pac-man.

### 2.world()

**descriptions:** it's used to draw the world using path, drawing the background in black and the walls in blue. It relies on the variation *tiles*, if tile > 0, it means it's not wall here,so that you can continue calculating the path's position, then using function **square()** to draw a square in blue representing paths. If tile = 1, we need to draw a dot on the path as the score chance.

**parameters:** it has no parameters particularly

**usage example:**

```python
def world():
    """Draw world using path."""
    # 绘制地图
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10) # move to the path's centre
                path.dot(2, 'white')
```

### 3.square()

**description:** draw square using path in (x,y)

**parameters:** x,y

**usage examples:**

```python
def square(x, y):
    """Draw square using path at (x, y)."""
    path.up()# stop drawing
    path.goto(x, y)# move to (x,y)
    path.down()# put down pen and begin drawing
    path.begin_fill()

    for count in range(4):# cycle 4 times because squares have 4 lines
        path.forward(20) # describe the length
        path.left(90) # describe the direction

    path.end_fill()
```

### move()

**description:** it's used to move Pac-man and all ghosts. In this function, Pac-man's aim and ghosts' positions will be checked whether valid or not, if valid, Pac-man's position will update through keyboard and ghosts' position will update through the recent direction through the ghost list. If invalid, Pac-man will stay the same, but ghosts need change their position randomly in options. By the way, the game needs update frequently, we set up a function to recall *move()* in 100s.

**usage example:**

```python
def move():
    """Move pacman and all ghosts."""
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim): #check the aim and position
        pacman.move(aim)

    index = offset(pacman) # calculate the index on map

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()#call function in Turtle to update the game window

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)
```

It's not very difficult to discover, we steal have something uncompleted. They are functions *offset()* and *valid()*, but we have one thing for certain, that *offset()* is building for calculating the index on the map while *valid()* for checking the position is valid or not(is that point on the map?). Then we can start in realize them.

### offset()

**usage example:**

```python
def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index
```

point.x is the x-coordinate of the given point, we use floor() to round down point.x to the nearest multiple of 20, +200 can shift the x-coordinate to align with the grids' origin, /20 converts the coordinate into a grid index by dividing by the tile size 20.

point.y has the same method, the only difference is 180- reverses the y-axis to match the grid's indexing(since the grid's origin is at the top-left corner).

### valid()

**usage example:**

```python
def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:#recent position
        return False

    index = offset(point + 19)

    if tiles[index] == 0:#wall
        return False

    return point.x % 20 == 0 or point.y % 20 == 0 #grid
```

it will check a position through walls, grids and recent position, then return a bool variation.

This is the whole code explanation of pacman.py. It's obvious that it can be better through several additions and changes. I'll talk about that in the NEXT PART.
