from tkinter import *
from tkinter import filedialog


def main():
    window = Tk()
    window.title("open and save")
    window.config(bg="#d9e4ff")
    window.resizable(width=False, height=False)

    text_area = Text(
        window, 
        width=58, 
        height=25, 
        font=("Arial", 15),
        bg="#d9e4ff", 
        fg="#25b2d9"
    )
    text_area.pack()

    open = Button(
        window,
        text="Open a file",
        font=("Arial", 20),
        bg="blue",
        fg="yellow",
        activebackground="blue",
        activeforeground="yellow",
        width=15,
        padx=30,
        pady=20,
        command=lambda: open_file(),
    )
    open.pack(side="left")

    save = Button(
        window,
        text="Save the text as a file",
        font=("Arial", 20),
        bg="blue",
        fg="#d9e4ff",
        activebackground="blue",
        activeforeground="#d9e4ff",
        width=18,
        padx=20,
        pady=20,
        command=lambda text=text_area: save_file(text),
    )
    save.pack(side="right")

    window.mainloop()


def open_file():
    path = filedialog.askopenfilename(
        initialdir=r"F:\mohamed files",
        title="Open file",
        filetypes=(("text files", "*.txt"), ("all files", "*.*")),
    )
    if path:
        with open(path) as file:
            print(file.read())


def save_file(text):
    file = filedialog.asksaveasfile(
        initialdir=r"F:\family",
        title="Save file",
        defaultextension=(".txt"),
        filetypes=[("text files", ".txt"), ("all files", ".*")],
    )
    if file:
        file_text = text.get("1.0", END)
        file.write(file_text)
        file.close()


if __name__ == "__main__":
    main()
