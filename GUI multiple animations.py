from tkinter import *
import time
import sys


class Ball:
    def __init__(self, canvas, x, y, diameter, xVelocity=1, yVelocity=1, color="black"):
        self.canvas = canvas
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.ball = canvas.create_oval(x, y, diameter, diameter, fill=color)

    def move(self):
        coordinates = self.canvas.coords(self.ball)
        if coordinates[0] < 0 or coordinates[2] >= self.canvas.winfo_width():
            self.xVelocity *= -1
        if coordinates[1] < 0 or coordinates[3] >= self.canvas.winfo_height():
            self.yVelocity *= -1

        self.canvas.move(self.ball, self.xVelocity, self.yVelocity)


def main():
    window = Tk()

    WIDTH = 500
    HEIGHT = 500

    canvas = Canvas(
        window, width=WIDTH, height=HEIGHT, bg="green", bd=0, highlightthickness=0
    )
    canvas.pack()

    volley_ball = Ball(canvas, 0, 0, 100, xVelocity=1, yVelocity=2, color="white")
    teniss_ball = Ball(canvas, 50, 50, 100, xVelocity=3, yVelocity=4, color="yellow")
    basket_ball = Ball(canvas, 100, 100, 175, xVelocity=3, yVelocity=2, color="orange")
    try:
        while True:
            volley_ball.move()
            teniss_ball.move()
            basket_ball.move()
            window.update()
            time.sleep(0.01)
    except TclError:
        sys.exit()


if __name__ == "__main__":
    main()
