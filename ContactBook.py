from tkinter import *
import sqlite3
from tkinter import messagebox
import re 
import sys

 
db = sqlite3.connect("mohamed phone book.db")
db.execute("CREATE TABLE IF NOT EXISTS person (name TEXT, phone_no TEXT)")

times =0
def main():
    global times 

    window = Tk()
    window.config(bg="#4dc1ff")
    window.title("mekawy phone book")
    x = int(window.winfo_screenwidth()/2 - 275)
    y = int(window.winfo_screenheight()/2 - 275)
    window.geometry(f"550x550+{x}+{y}")
    window.resizable(width=False, height=False)

    # name label and its entry box of text 
    Label(window, text="NAME", font=("Arial", 15), bg="#4dc1ff").place(x=20, y=20)
    name_entry = Entry(window, font=("Arial", 15))
    name_entry.place(x=155, y=20)
    # phone number label and its entry box of text
    Label(window, text="PHONE NO.", font=("Arial", 15), bg="#4dc1ff").place(x=20, y=70)
    phone_entry = Entry(window, font=("Arial", 15))
    phone_entry.place(x=155, y=70)

    # names list
    frame = Frame(window)
    frame.place(x=310, y=150)

    name_list = Listbox(frame, width=20, height=12, bg="#daf553", selectforeground="#08489c", selectbackground="#3be2f5", font=("Constantia", 15))
    name_list.pack(side=LEFT)

    phones = get_names_phone()
    for phone in phones:
        name_list.insert(times, phone)
        times += 1

    # scroll bar 
    scroll_bar = Scrollbar(frame)
    scroll_bar.pack(side=RIGHT, fill=Y)
    name_list.config(yscrollcommand=scroll_bar.set)

    # add person button
    add_button = Button(window, bg="#546b69", text="ADD", font=("consolase", 15), activebackground="#546b69", command=lambda : add(name_entry, phone_entry, name_list))
    add_button.place(x=40, y=150)
    # view phone number button
    view_button = Button(window, bg="#546b69", text="VIEW", font=("consolase", 15), activebackground="#546b69", command=lambda : view(name_list))
    view_button.place(x=40, y=210)
    # delete person button
    delete_button = Button(window, bg="#546b69", text="DELETE", font=("consolase", 15), activebackground="#546b69", command=lambda : delete(name_list))
    delete_button.place(x=40, y=270)
    # edit name or phone number button
    edit_button = Button(window, bg="#546b69", text="EDIT", font=("consolase", 15), activebackground="#546b69", command=lambda : edit(name_list))
    edit_button.place(x=40, y=330)
    # reset all button
    reset_button = Button(window, bg="#546b69", text="RESET", font=("consolase", 15), activebackground="#546b69", command=lambda : reset(name_entry, phone_entry))
    reset_button.place(x=40, y=390)
    # exit button
    exit_button = Button(window, bg="red", text="EXIT", font=("Arial", 15), activebackground="red", command=save_and_quit)
    exit_button.place(x=480, y=480)

    window.mainloop()


def add(name_entry, phone_entry, name_list):
    global times

    name = name_entry.get().strip().capitalize()
    phone_number = phone_entry.get().strip()
    form = re.search(r"(^(?:\D?(\d)\D)(\d{3})\D?(\d{3})\D?(\d{4})$)|(?:^\D?(\d{3})\D?(\d{4})\D?(\d{4})$)", phone_number)
    if name == "" or len(name) > 15:
        messagebox.showerror("name", "Invalid name")
    elif form == None:
        messagebox.showerror("phone.no", "Invalid phone number")
    else:
        phone_number = ""
        for num in form.groups():
            if num:
                phone_number += "-" + num 


        cur = db.cursor()
        cur.execute("SELECT phone_no FROM person WHERE name =? ", (name, ))
        if not (cur.fetchone()):          
            name_list.insert(times, name)
            times += 1

        db.execute("INSERT INTO person (name, phone_no) VALUES (?, ?)", (name, phone_number))
        messagebox.showinfo("added", "added successfully!")

def view(name_list):
    cur = db.cursor()
    name = get_selected(name_list)
    if name == None:
        return

    cur.execute("SELECT phone_no FROM person WHERE name =? ", (name, ))
    phone_nums = cur.fetchall()

    # create a window with a list box inside it and a scroll bar
    phone_window = Toplevel()
    list = Listbox(phone_window, width=20, height=12, bg="#fcab14", selectforeground="#423cfa", selectbackground="#ffd373", font=("Clement Numbers", 20))
    list.pack(side=LEFT)
    scroll_bar = Scrollbar(phone_window)
    scroll_bar.pack(side=RIGHT, fill=Y)
    list.config(yscrollcommand=scroll_bar.set)

    for index, phone_num in enumerate(phone_nums):
        list.insert(index, phone_num)


def delete(name_list):
    name = get_selected(name_list)
    if name == None:
        return
    
    name_list.delete(name_list.curselection())

    cur = db.cursor()
    cur.execute("DELETE FROM person WHERE name=?", (name, ))
    messagebox.showinfo("success", "deleted successfully!")


def edit(name_list):
    name = get_selected(name_list)
    ask_window = Toplevel()
    entrybox = Entry(ask_window, width=20, font=("Clement Numbers", 20), bg="#fcab14", fg="#423cfa")
    entrybox.pack(side=LEFT)

    button = Button(ask_window, bg="blue", activebackground="blue", fg="white", text="Edit", font=("Arial", 15), command=lambda : finish(entrybox, name, ask_window))
    button.pack(side=RIGHT)
    
def finish(entrybox, name, win):
    new_phone = entrybox.get()
    result = re.search(r"(^(?:\D?(\d)\D)(\d{3})\D?(\d{3})\D?(\d{4})$)|(?:^\D?(\d{3})\D?(\d{4})\D?(\d{4})$)", new_phone)
    if not result:
        messagebox.showerror("phone.no", "Invalid phone number")
        return
    if name == None:
        return

    cur = db.cursor()
    cur.execute("UPDATE person SET phone_no=? WHERE name=?", (new_phone, name))

    win.destroy()
    messagebox.showinfo("updated", "edited successfully!")

def reset(name_entry, phone_entry):
    name_entry.delete(0, END)
    phone_entry.delete(0, END)


def save_and_quit():
    db.commit()
    db.close()
    sys.exit()


def get_names_phone():
    formated_names = [] # a list with no duplicates
    cur = db.cursor()
    cur.execute("SELECT name FROM person")
    names = cur.fetchall()
    for name in names:
        if name not in formated_names:
            formated_names.append(name)

    return sorted(formated_names)


def get_selected(name_list):
    index = name_list.curselection()
    if not index:
        messagebox.showerror("select error", "Select a name to view its number first!")
        return None

    if type(name_list.get(index)) is str:
        name = name_list.get(index)
    elif type(name_list.get(index)) is tuple:
        name, = name_list.get(index)
    else:
        return None

    return name



if __name__ == "__main__":
    main()
    db.commit()
    db.close()