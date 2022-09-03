from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00ff00"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
DIRECTION = "down"
SCORE = 0

class Snake:
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)



class Food:
    def __init__(self, canvas):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(x , y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def main():
    window = Tk()
    window.title("snake game")
    window.resizable(width=False, height=False)

    score_label = Label(window, text=f"score: {SCORE}", font=("Clement Numbers", 20))
    score_label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH, highlightbackground="#38b6f5")
    canvas.pack()

    window.update()

    win_width = window.winfo_width()
    win_height = window.winfo_height()
    x =int(window.winfo_screenwidth()/2 - win_width/2)
    y = int(window.winfo_screenheight()/2 - win_height/2)

    window.geometry(f"{win_width}x{win_height}+{x}+{y}")

    window.bind("<Left>", lambda event: change_direction("left"))
    window.bind("<Right>", lambda event: change_direction("right"))
    window.bind("<Down>", lambda event: change_direction("down"))
    window.bind("<Up>", lambda event: change_direction("up"))


    snake = Snake(canvas)
    food = Food(canvas)
    next_turn(snake, food, window, canvas, score_label)

    window.mainloop()


def next_turn(snake, food, window, canvas, score_label):
    global SCORE

    x, y = snake.coordinates[0]
    if DIRECTION == "up":
        y -= SPACE_SIZE
    elif DIRECTION == "down":
        y += SPACE_SIZE
    elif DIRECTION == "left":
        x -= SPACE_SIZE
    elif DIRECTION == "right":
        x += SPACE_SIZE

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    snake.coordinates.insert(0, [x, y])

    if x == food.coordinates[0] and y == food.coordinates[1]:
        SCORE += 1
        score_label.config(text=f"score: {SCORE}")
        canvas.delete("food")
        food = Food(canvas)
    else:
        canvas.delete(snake.squares[-1])
        del snake.coordinates[-1]
        del snake.squares[-1]

    if check_collistions(snake):
        game_over(canvas)
    else:
        window.after(SPEED, next_turn, snake, food, window, canvas, score_label)

def change_direction(new_direction):
    global DIRECTION
    if new_direction == "left":
        if DIRECTION != "right":
            DIRECTION = new_direction

    elif new_direction == "right":
        if DIRECTION != "left":
            DIRECTION = new_direction

    elif new_direction == "up":
        if DIRECTION != "down":
            DIRECTION = new_direction

    elif new_direction == "down":
        if DIRECTION != "up":
            DIRECTION = new_direction

def check_collistions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
        else:
            return False

def game_over(canvas):
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, 
                        font=("consolas", 70), text="GAME OVER", fill="red", tag="game over")

if __name__ == "__main__":
    main()