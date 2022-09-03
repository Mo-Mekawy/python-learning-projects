import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *




def main():
    window = Tk()
    window.title("Mekawy mohamed text editor")
    window_width = 500
    window_height = 500

    # get middle screen coordinates to put window on it
    x = int((window.winfo_screenwidth()/2) - window_width/2)
    y = int((window.winfo_screenheight()/2) - window_height/2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # make a variable for font name and size and set them to defualt value
    font_name = StringVar()
    font_name.set("Arial")
    font_size = StringVar()
    font_size.set(25)

    # make a text box
    text_area = Text(window, font=(font_name.get(), font_size.get()))
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    text_area.grid(sticky=N + E + W + S)
    # make a scroll bar
    scroll_bar = Scrollbar(text_area)
    scroll_bar.pack(side=RIGHT, fill=Y)
    text_area.config(yscrollcommand=scroll_bar.set)
    # make buttons
    frame = Frame(window)
    frame.grid()
    # make a color button
    color_button = Button(frame, text="color", command= lambda text=text_area:change_color(text))
    color_button.grid(row=0, column=0)
    # make a menu for font names
    font_box = OptionMenu(frame, font_name, *font.families(), command=lambda name=font_name :change_font(name, font_size, text_area))
    font_box.grid(row=0, column=1)
    # make a spinbox for font size
    size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=lambda size=font_size :change_font(font_name.get(), size, text_area))
    size_box.grid(row=0, column=2)
    
    # create a option menu
    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    # create a file menu and add it
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    # create command in the file menu 
    file_menu.add_command(label="New", command=lambda :new_file(window, text_area))
    file_menu.add_command(label="Open", command=lambda :open_file(window, text_area))
    file_menu.add_command(label="Save", command=lambda :save_file(window, text_area))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=lambda :quit(window))

    # create an edit menu and add it
    edit_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    # create command in the edit menu 
    edit_menu.add_command(label="Copy", command=lambda :copy(text_area))
    edit_menu.add_command(label="Cut", command=lambda :cut(text_area))
    edit_menu.add_command(label="Paste", command=lambda :paste(text_area))

    # create a help menu and add it
    help_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    # create command in the help menu 
    help_menu.add_command(label="About", command=about)
    file = None




    window.mainloop()


def change_color(text_area):
    color = colorchooser.askcolor(title="pick a color")
    text_area.config(fg=color[1])

def change_font(name, size, text_area):
    text_area.config(font=(name, size.get()))

def new_file(window, text_area):
    window.title("Untitled")
    text_area.delete(1.0, END)

def open_file(window, text_area):
    path = filedialog.askopenfilename(
        initialdir=r"F:\mohamed files",
        title="Open file",
        defaultextension=".txt",
        filetypes=(("text Documents", "*.txt"), ("all files", "*.*")),
    )
    if path:
        window.title(os.path.basename(path))
        text_area.delete(1.0, END)

        with open(path) as file:
            text_area.insert(1.0, file.read())
            

def save_file(window, text_area):
    path = filedialog.asksaveasfilename(
        initialdir=r"F:\family",
        title="Save file",
        defaultextension=(".txt"),
        filetypes=[("text files", ".txt"), ("all files", ".*")],
    )
    if path:
        with open(path, "w") as file:
            window.title(os.path.basename(path))
            file_text = text_area.get("1.0", END)
            file.write(file_text)


def copy(text_area):
    text_area.event_generate("<<Copy>>")

def cut(text_area):
    text_area.event_generate("<<Cut>>")

def paste(text_area):
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("About this program", "This is a program written by mohamed mekawy")

def quit(window):
    window.destroy()



if __name__ == "__main__":
    main()