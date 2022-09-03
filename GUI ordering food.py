"""show a GUI that displays food so you can order what you want"""
from tkinter import *


class Food:
    """
    class that istantiate an object that make food by
    (make_radio_btns) and to display it with (start)
    params:
    food= (a dict that has the name of the food as key and path to its image as the value)
    """

    def __init__(self, foods) -> None:
        self.root = Tk()
        self.foods = foods
        self.root.resizable(width=False, height=False)
        self.root.config(bg="green")

        self.icons = []
        self.x = IntVar()
        self.radio_btns = []

    def make_radio_btns(self):
        for index, food in enumerate(self.foods):
            self.icons.append(PhotoImage(file=self.foods[food]))
            radio_btn = Radiobutton(
                self.root,
                text=food,
                font=("Impact", 50),
                bg="green",
                fg="blue",
                indicatoron=0,
                width=500,
                activebackground="green",
                activeforeground="blue",
                image=self.icons[index],
                compound="left",
                padx=25,
                pady=10,
                variable=self.x,
                value=index,
                command=lambda: print(
                    f"You ordered {self.radio_btns[self.x.get()]['text']}"
                ),
            )
            radio_btn.deselect()
            radio_btn.pack(anchor=W)
            self.radio_btns.append(radio_btn)

    def start(self):
        self.root.mainloop()


def main():
    foods = {
        "pizza": r"F:\mohamed files\images\pizza.png",
        "hamburger": r"F:\mohamed files\images\hamburger.png",
        "hotdog": r"F:\mohamed files\images\hotdog.png",
    }

    food = Food(foods=foods)
    food.make_radio_btns()
    food.start()


if __name__ == "__main__":
    main()
