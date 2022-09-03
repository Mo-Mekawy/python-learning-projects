import turtle
import time

# speed
ball_spd = 2  # speed of the ball
rack_spd = 60  # speed of the rackets

wind = turtle.Screen()  # initialize a screen to do the work on
# remove the maximize option from the screen
wind.cv._rootwindow.resizable(False, False)
# title the game (ping pong by mohamed mekawy)
wind.title("ping pong by mohamed mekawy")
wind.bgcolor("black")  # set its color to black
wind.setup(width=800, height=600)  # set its size
wind.tracer(0)  # disable auto update

# racket1
racket1 = turtle.Turtle()  # make a racket as turtle object
racket1.speed(0)  # make the draw(animation) speed as the fastest option
racket1.shape("square")  # make it as an square
racket1.color("blue")  # make its color blue
# make stretch it so its more like a racket not a square
racket1.shapesize(stretch_wid=5, stretch_len=1)
racket1.penup()  # disable the the racket`s ability of drawing lines
# finally draw that racket at the left middle of the screen
racket1.goto(-350, 0)

# racket2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("red")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.penup()
racket2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_spd  # make the ball move with a slope
ball.dy = ball_spd

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 270)
score.write(f"player1:{score1} || player2:{score2}",
            align="center", font=("courier", 15, "normal"))

# countdown
timeleft = turtle.Turtle()
timeleft.speed(0)
timeleft.color("white")
timeleft.penup()
timeleft.hideturtle()
timeleft.goto(-340, 270)

# functions


def racket1_up():
    racket1.sety(racket1.ycor() + rack_spd)  # move the first racket up


def racket1_down():
    racket1.sety(racket1.ycor() - rack_spd)  # move the first racket down


def racket2_up():
    racket2.sety(racket2.ycor() + rack_spd)  # move the second racket up


def racket2_down():
    racket2.sety(racket2.ycor() - rack_spd)  # move the second racket down


wind.listen()  # check if there is a key being pressed
# if the w key is pressed move the first racket up
wind.onkeypress(racket1_up, "w")
# if the s key is pressed move the first racket down
wind.onkeypress(racket1_down, "s")
# if the up arrow is pressed move the second racket up
wind.onkeypress(racket2_up, "Up")
# if the down arrow is pressed move the second racket down
wind.onkeypress(racket2_down, "Down")

start = time.time()
limit = 120  # the timer limit
# game loop
while(time.time() - start) < limit:
    # window
    wind.update()  # update the screen
    # update the ball`s position so it moves with a slope
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # countdown
    t = limit - int(time.time() - start)
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    timeleft.clear()
    timeleft.write(f"timeleft:{timer}", align="center",
                   font=("courier", 10, "normal"))

    # score
    score.clear()  # remove the previous score
    score.write(f"player1:{score1} || player2:{score2}", align="center", font=(
        "courier", 15, "normal"))  # write the new score

    # game
    # if the ball touched the upper or lower edge of the screen make it bounce
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:  # if the ball touched the right edge of the screen
        ball.goto(0, 0)  # move it to the center
        ball.dx *= -1
        score1 += 1

    if ball.xcor() < -390:  # if the ball touched the left edge of the screen
        ball.goto(0, 0)  # move it to the center
        ball.dx *= -1
        score2 += 1

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() <= (racket2.ycor() + 40) and ball.ycor() >= (racket2.ycor() - 40):  # if the ball hit the racket make it bounce
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() <= (racket1.ycor() + 40) and ball.ycor() >= (racket1.ycor() - 40):  # if the ball hit the racket make it bounce
        ball.setx(-340)
        ball.dx *= -1
score.clear()
timeleft.clear()
if score1 > score2:
    score.write(f"player1 is the winner {score1}>{score2}", align="center", font=(
        "courier", 20, "normal"))
elif score2 > score1:
    score.write(f"player2 is the winner {score2}>{score1}", align="center", font=(
        "courier", 20, "normal"))
else:
    score.write(f"It is a draw {score1}={score2}",
                align="center", font=("courier", 20, "normal"))
time.sleep(5)
