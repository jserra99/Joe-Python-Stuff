# a121_catch_a_turtle.py
#-----import statements-----
import turtle as tt
import random as rand
import leaderboard as lb

#-----game configuration----
turtle_color = "white"
turtle_size = 3
turtle_shape = "circle"
tt.bgcolor("black")
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("What is your name?: ")

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

#-----initialize turtle-----
spot = tt.Turtle()
spot.color(turtle_color)
spot.shapesize(turtle_size)
spot.shape(turtle_shape)
spot.pu()
manage_leaderboard()
score_writer = tt.Turtle()
score_writer.pu()
score_writer.goto(190, 140)
score_writer.color("white")
score_writer.hideturtle()
counter = tt.Turtle()
counter.color("white")
counter.pu()
counter.goto(-190, 140)
counter.hideturtle()
#-----game functions--------
def when_clicked(i, j):
    global timer, turtle_size
    if (timer_up == False):
        spot.color("red")
        spot.stamp()
        spot.color(turtle_color)
        turtle_size -= .05
        spot.shapesize(turtle_size)
        update_score()
        change_position()
    else:
        spot.hideturtle()

def  change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.goto(new_xpos, new_ypos)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write("Score: " + str(score), font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
spot.onclick(when_clicked)
wn = tt.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()