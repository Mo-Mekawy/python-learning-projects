from tkinter import *  
import random

players = ["x", "o"]
player = random.choice(players)
def main():
    window = Tk()
    window.title("Tic-Tac-Toe")

    buttons = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

    label = Label(window, text=f"{player} turn", font=("Arial", 20))
    label.pack(side=TOP)

    reset_button = Button(text="restart", font=("consolas", 20), 
                command=lambda label=label, buttons=buttons: new_game(buttons, label))
    reset_button.pack(side=TOP)

    frame = Frame(window)
    frame.pack()
    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", font=("consolas", 20), width=5, height=2, bd=2,
                                        command= lambda row=row, column=column : next_turn(row, column, buttons, label))
            buttons[row][column].grid(row=row, column=column)

    window.mainloop()

def next_turn(row, column, buttons, label):
    global player
    if buttons[row][column]["text"] =="" and check_winner(buttons, label) == False and empty_spaces(buttons):
        if player == "x":
            buttons[row][column]["text"] = "x"
            if check_winner(buttons, label) == False:
                player = "o"
                label.config(text=f"{player} turn")
            elif check_winner(buttons, label):
                label.config(text=f"{player} wins")
        else:
            buttons[row][column]["text"] = "o"
            if check_winner(buttons, label) == False:
                player = "x"
                label.config(text=f"{player} turn")
            elif check_winner(buttons, label):
                label.config(text=f"{player} wins")
        
def check_winner(buttons, label):
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"]  == buttons[row][2]["text"] !="":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"]  == buttons[2][column]["text"] !="":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] !="":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    if buttons[2][0]["text"] == buttons[1][1]["text"] == buttons[0][2]["text"] !="":
        buttons[2][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[0][2].config(bg="green")
        return True

    if empty_spaces(buttons) == False:
        label.config(text="Tie!")   
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return None

    return False

def empty_spaces(buttons):
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def new_game(buttons, label):
    global players
    global player

    player = random.choice(players)

    label.config(text=f"{player} turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#f0f0f0")

if __name__ == "__main__":
    main()