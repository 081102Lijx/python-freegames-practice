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