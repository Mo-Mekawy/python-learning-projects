from tkinter import *


def create_resturant():
    # create window and set its name and size and bg color
    window = Tk()
    window.title("Mohamed resturant")
    window.geometry("600x380")
    icon = PhotoImage(file=r"F:\mohamed files\images\hamburger.png")
    window.iconphoto(True, icon)
    window.config(bg="#fc8647")
    window.resizable(width=False, height=False)
    """----------------------------------------------------------------------"""
    # create pizza image on the left
    pizza = PhotoImage(file=r"F:\mohamed files\images\pizza.png")
    label1 = Label(window, image=pizza, compound="center", bg="#fc8647")
    label1.place(x=0, y=150)

    # create hotdog image on the right
    hotdog = PhotoImage(file=r"F:\mohamed files\images\hotdog.png")
    label2 = Label(window, image=hotdog, compound="center", bg="#fc8647")
    label2.place(x=450, y=150)
    """----------------------------------------------------------------------"""
    # create a list box to order food
    listbox = Listbox(
        window,
        width=20,
        bg="#63f2ff",
        font=("Constantia", 15),
        selectforeground="yellow",
        selectmode=MULTIPLE,
    )
    listbox.pack()
    listbox.insert(1, "Pizza")
    listbox.insert(2, "Hamburger")
    listbox.insert(3, "Hotdog")
    listbox.insert(4, "Pasta")
    listbox.insert(5, "Salad")
    listbox.insert(6, "Shawirma")
    listbox.insert(7, "Kabab")
    listbox.insert(8, "Kushari")
    listbox.insert(9, "Soup")
    listbox.config(height=listbox.size())
    """----------------------------------------------------------------------"""
    # create submit button
    submit = Button(
        window,
        text="order",
        font=("Arial", 15),
        width=20,
        bg="green",
        fg="blue",
        activebackground="green",
        activeforeground="blue",
        command=lambda listbox=listbox: order(listbox),
    )
    submit.pack()
    """----------------------------------------------------------------------"""
    # create an entry box to add custom food
    entrybox = Entry(window, font=("Arial", 15), fg="#20e820", bg="#035082")
    entrybox.insert(0, "enter a custom food")
    entrybox.bind("<1>", lambda _: entrybox.delete(0, END))
    entrybox.pack()

    add = Button(
        window,
        text="Add",
        font=("Arial", 15),
        width=20,
        bg="#909191",
        fg="#d3f069",
        activebackground="#909191",
        activeforeground="#d3f069",
        command=lambda listbox=listbox, entrybox=entrybox: insert(listbox, entrybox),
    )
    add.pack()

    delete = Button(
        window,
        text="Delete",
        font=("Arial", 15),
        width=20,
        bg="#909191",
        fg="#d3f069",
        activebackground="#909191",
        activeforeground="#d3f069",
        command=lambda listbox=listbox: pop(listbox),
    )
    delete.pack()
    window.mainloop()


def order(listbox):
    foods = []
    for index in listbox.curselection():
        foods.insert(index, listbox.get(index))

    if foods:
        print(f"you have ordered:", end=" ")
        for food in foods:
            print(food, end=", ")
        print()


def insert(listbox, entrybox):
    text = entrybox.get()
    if text and text != "enter a custom food":
        listbox.insert(listbox.size(), text)
        listbox.config(height=listbox.size())


def pop(listbox):
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())


def main():
    create_resturant()


if __name__ == "__main__":
    main()
