######################################################
# Project: <Project 2>
# UIN: <667689607>
# repl.it URL: <https://replit.com/@CS111-Fall2021/Project-2-MuhammadSiddiq9#main.py>

# For this project, I received help from the following members of CS111.
# Imran Khan, netID:654046372 helped with key press events and movement for the player
 
######################################################

# these are the modules we imported so that we can utilize the random and turtle functions
import turtle
import random

# this poriton initilaizes the screen so that we can use it and also sets the background
s = turtle.Screen()
s.setup(320,320)
s.screensize(300,300)
s.bgcolor("black")
s.bgpic("pacmanbg.gif")
s.tracer(0)
w, h = s.screensize()

# this portion intiliazes the turtles and hides them, so that we can use them for displaying elements
t1 = turtle.Turtle()
t1.ht()
t2= turtle.Turtle()
t2.ht()
t3 = turtle.Turtle()
t3.ht()
t4 = turtle.Turtle()
t4.ht()

# this is where we create our global variables that will be used throughout the main function
game_state = False
num_lives = 3
score = 0
speed = 0.1
level = 1

# this is our dictinary of game objects that we will use to store the player and harm object information
game_objects = [{"t": turtle.Turtle(),"x":0, "y":125, "radius": 12, "image":"goldcoin.gif", "type":"goldcoin"},{"t": turtle.Turtle(),"x":50, "y":75, "radius": 12, "image":"ghost.gif", "type":"ghost1"},{"t": turtle.Turtle(),"x":-50, "y":25, "radius": 12, "image":"ghost.gif", "type":"ghost2"},{"t": turtle.Turtle(),"x":-10, "y":-25, "radius": 12, "image":"ghost.gif", "type":"ghost1"}, {"t": turtle.Turtle(),"x":-100, "y":-75, "radius": 12, "image":"ghost.gif", "type":"ghost2"},{"t": turtle.Turtle(),"x":0, "y":-125, "radius": 12, "image":"pacman.gif", "type":"pacman"}
  ]

# this is a dictinary of random y values that the goal objective will randomly sort through. It is only multiples of 50 as the screen has been divided into  a 6x6 play field
random_y = [-150,-100,-50,50,100,150]

def wall_collision():
  ''' this is a function that checks for the wall collision of pacman and the ghost. If they do collid with a wall, they will get sent back on the opposite edge'''
  # the if statements check if the player or harm object has gone over the edge based on its x position and the x position of the wall minus the radius. It then sets the x position to the opposite edge.
  for obj in game_objects:
    if (obj["type"] == "ghost1") and obj['x']> (150 + obj['radius']) :
      obj["x"] = -w/2
    elif (obj["type"] == "ghost2") and obj['x']<(-150 - obj["radius"]):
      obj["x"] = w/2
    elif (obj["type"] == "pacman") and obj['x']> (150 + obj['radius']):
      obj["x"] = -w/2
    elif (obj["type"] == "pacman") and obj['x']< (-150 - obj['radius']):
      obj["x"] = w/2
    elif (obj['type'] == 'pacman') and obj['y']< (-125):
      obj["y"] = -125
    elif (obj['type'] == 'pacman') and obj['y'] > (125):
      obj["y"] = 125

def animate_image():
  ''' this function loops through the game_object dictinary and animates the different elements based on the x,y, and t value'''
  for obj in game_objects:
    
      t = obj["t"]
      x = obj["x"]
      y = obj["y"]

      t.goto(x, y) 

def reset_position():
  ''' this function is used in the check_collision function in order to rest the position of the player if they make collision'''
  game_objects[5]['t'].goto(0,-135)
  game_objects[5]['x'] = 0
  game_objects[5]['y'] = -135

def change_lives():
  ''' this function changes the num of lives left after collision and rewrites it'''
  global num_lives
  num_lives -= 1
  t3.penup()
  t3.goto(120,130)
  t3.color("white")
  t3.pendown()
  t3.clear()
  t3.write(f'Lives:{num_lives}',font= 'Arial', align = 'center')

def change_score():
  ''' this function changes the score of the player and rewrites it'''
  global score
  score += 15
  t1.penup()
  t1.goto(-145,- 140)
  t1.color("white")
  t1.pendown()
  t1.clear()
  t1.write(f'Score:{score}',font= 'Arial', align = 'left') 

def change_level():
  ''' this function changes the level of the player and rewrites it'''
  global level
  global speed
  level += 1
  t2.penup()
  t2.goto(-145,130)
  t2.color("white")
  t2.pendown()
  t2.clear()
  t2.write(f'Level:{level}',font= 'Arial', align = 'left')
  speed += 0.025

def check_collision():
  ''' this function checks for collision based on the distance between the player and the harm objects/objective and then resets the position and changes the lives,level or score'''
  # these if statements check to see if the distance between the harm/objective to the player is less than the combined radius of the two. This is a way to see if the objects are colliding 
  for obj in game_objects:
      if game_objects[1]['t'].distance(game_objects[5]['t']) <= game_objects[1]['radius'] + game_objects[4]['radius']:
        reset_position()
        change_lives()
      if game_objects[2]['t'].distance(game_objects[5]['t']) <= game_objects[1]['radius'] + game_objects[4]['radius']:
        reset_position()
        change_lives()
      if game_objects[3]['t'].distance(game_objects[5]['t']) <= game_objects[2]['radius'] + game_objects[4]['radius']:
        reset_position()
        change_lives()
      if game_objects[4]['t'].distance(game_objects[5]['t']) <= game_objects[3]['radius'] + game_objects[4]['radius']:
        reset_position()
        change_lives()
      if game_objects[0]['t'].distance(game_objects[5]['t']) <= game_objects[3]['radius'] + game_objects[4]['radius']:
        reset_position()
        game_objects[0]['x'] =random.choice(random_y)
        change_score()
        change_level()

def draw_initialscore():
  ''' this function draws the intial score to display 0 so that it still shows at the start of the animation loop'''
  t1.penup()
  t1.goto(-145,-140)
  t1.color("white")
  t1.pendown()
  t1.clear()
  t1.write(f'Score:{0}',font= 'Arial', align = 'left') 

def draw_initiallives():
  ''' this function draws the intial lives to display 3 so that it still shows at the start of the animation loop'''
  t3.penup()
  t3.goto(120,130)
  t3.color("white")
  t3.pendown()
  t3.clear()
  t3.write(f'Lives:{num_lives}',font= 'Arial', align = 'center')

def draw_initallevel():
  ''' this function draws the intial level to display 1 so that it still shows at the start of the animation loop'''
  t2.penup()
  t2.goto(-145,130)
  t2.color("white")
  t2.pendown()
  t2.clear()
  t2.write(f'Level:{1}',font= 'Arial', align = 'left')


def end_screen():
  ''' this function is the end screen that will be displayed when the player loses and displays the total score'''
  global score
  s.clear()
  t1.penup()
  t1.goto(0,30)
  t1.color("purple")
  t1.pendown()
  t1.clear()
  t1.write(f'GAME OVER',font= 'Arial', align = 'CENTER')
  t1.penup()
  t1.goto(0,0)
  t1.pendown()
  t1.write(f'Total Score: {score}',font= 'Arial', align = 'CENTER')

def start_screen():
  ''' this is the start screen function that gives the player instructions on how to play and start the game'''
  global game_state
  # the start screen will only run if the game state is False, meaning that the game is not currently running
  if game_state == False:
    t4.color("Yellow")
    t4.penup()
    t4.goto(0,0)
    t4.pendown()
    t4.write('PACMAN HOPPER',font= ("Arial",10), align = 'center')
    t4.penup()
    t4.goto(0,-25)
    t4.pendown()
    t4.write('PRESS SPACEBAR TO PLAY',font=("Arial",10), align = 'center')
    t4.penup()
    t4.goto(0,-50)
    t4.pendown()
    t4.write('Navigate Pac-man through the ghost in order to reach the coin!',font=("Arial",7), align = 'center')



def animation_loop():
    ''' this is the entirety of the animation loop that runs when the player starts the game after the start screen'''
    # the rest of the animation loop will only run if the game state is set to true. This is why that is defined at the start.
    game_state = True
    t4.clear()
    if game_state == True:
      draw_initialscore()
      draw_initiallives()
      draw_initallevel()
    
    # this while statement only runs when the game state is set to true or the player has lives left
    while (game_state == True) and num_lives > 0:
      # this clears the last position of the object so that it can be redrawn in another position to make it look animated 
      for obj in game_objects:
        obj["t"].clear()

      # this is used to increase and decrease the x values so that the harm is in a different position each time
      for obj in game_objects:
        if (obj["type"] == "ghost1"):
          obj["x"] += speed
        if (obj["type"] == "ghost2"):
          obj["x"] -= speed
        
      
      wall_collision()

      animate_image()

    
      check_collision()
      s.update()
    
    # the end screen will only be run once the number of lives is equal to 0
    if num_lives == 0:
      end_screen()

def move_player():
  ''' this function allows the player to move based on the onkey presses that they input '''
  for obj in game_objects:
    if (obj['type'] == 'pacman'):
      def left():
        obj['x'] -= 50
      def right():
        obj['x'] += 50
      def up():
        obj['y'] += 50
      def down():
        obj['y'] -= 50


  s.listen()
  s.onkey(left,'Left')
  s.onkey(right,'Right')
  s.onkey(up,'Up')
  s.onkey(down,"Down")
  # this onkey event is used at the start screen. Once the spacebar is pressed, the animation loop is run.
  s.onkey(animation_loop, "space")


def add_shape():
  ''' this function loops through the game object dictionary and adds the image to the objects'''
  for obj in game_objects:
    s.addshape(obj["image"])
    obj["t"].shape(obj["image"])


def main(): 
  ''' this is the main function that encompasses all the other functions so that it is the only one that needs to be run'''
  global game_state

  add_shape()

  move_player()

  start_screen()
  
   
main()