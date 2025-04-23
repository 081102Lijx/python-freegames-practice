Typing speed is a marvelous characteristic for an engineer. TYPING is such a little game to improve one's typing speed.

# Comprehension

## Dependencies

We leverage the following core libraries for system implementation:

- random
- turtle
- string(used in this code to import *ascii_lowercase*, which is a string containing all lowercase English letters)

## Global variations

This section outlines the global variables used throughout the project,their purpose,and how they can be utilized.

- **targets = []**: used to store the positions of the falling letters
- **letters = []**: stores  the characters(letters) that correspond to the falling targets. Each letter in the letters list matches a position in the targets list.
- **score = 0**: used to store playing score.

## Running Logic

This section details the running logic of the game, converting the progress of a running circle,explaining functions of several core code.

```python
setup(420,420,370,0)
```

It's used to set up position and size of game window.

```python
hideturtle()
up()
tracer(False)
```

hideturtle() and tracer(False) are used to hide trace of turtle, the same as the pacman.py.

The up() function in the turtle module is used to lift the turtle's pen off the drawing surface. When the pen is "up", the turtle can move to a new position without drawing a line.

```python
listen()
for letter in ascii_lowercase:
    onkey(lambda letter=letter:press(letter),letter)
```

These code are used to listen to keyboard, and update scores through function **press()**

```python
move()
done()
```

These are key functions in typing.py. move() is used to change the letters' positions, I will explain it later. done() is called for maintaining the game window.

This is the running code of typing.py, after these functions, we can build a easy typing game in python. But that's not enough, we still have several questions.

- How to realize functions?
- How to change targets for better gaming experience?

## Functions

This section lists the main functions available in the projects along with their **descriptions**, **parameters** and **usage examples**.

**1. press(key):** 

**descriptions:** this function handles the player's input when they type a key. It checks if the pressed key matches any of the falling letters and updates the game state accordingly.

**parameters:****

- key: The key pressed by player
- score(global): Allows the function to modify score variable

**usage example:**

```python
def press(key):
    global score
    
    if key in letters:
        score += 1
        pos = letters.index(key)
        del targets[pos]
        del letters[pos]
    else:
        score -= 1
    print('Score:',score)
```

**2.move():**

**description:** The move() function is responsible for managing the movement of the falling letters and updating the game state. It handles the creation of new letters, and the game's animation loop.

**usage example:**

```python
def move():
    if randrange(20) == 0:
        x = randrange(-150, 150)
        target = vector(x, 200)
        targets.append(target)
        letter = choice(ascii_lowercase)
        letters.append(letter)

    for target in targets:
        target.y -= 1

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 100)
```

It will randomly draw letters , and control the letters falling down from the top of game window. If letter falls down on the bottom of game window, end the game.

**3.draw()**

**description:** The draw() function is responsible for rendering the falling letters on the screen. It clears the screen, iterates through the list of letters and their positions, and redraws them at their updated locations.

**usage example:** 

```python
def draw():
    clear()
    
    for target.letter in zip(targets,letters):
        goto(target.x,target.y)
        write(letter,align='center',font=('Consolas',20,'mormal'))
        
    update()
```

zip(targets,letters) can combine the targets list (positions of the letters) and the letters list(the actual letters) into pairs.

write(letter,align='Center',font=('Consolas',20,'normal')) draws the letter at the specified position using the specified font and alignment.

**4.draw()**

**description:** This function is used to check whether the position is valid in the game window.

**usage example:** 

```python
def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200
```

This is whole code explanation of typing.py. As a training game, these functions are not enough, it can be more interesting. I will talk about that LATER ON. 