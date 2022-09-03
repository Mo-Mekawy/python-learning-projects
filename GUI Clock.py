from threading import Thread
from tkinter import *
import time
import sys


def main():
    window = Tk()
    window.resizable(width=False, height=False)
    window.config(bg="#0cc0e8")
    window.title("Clock")

    time_label = Label(window, font=("Arial", 50), fg="green", bg="black", width=12)
    time_label.pack()

    day_label = Label(window, font=("Ink Free", 25), bg="#0cc0e8")
    day_label.pack()

    date_label = Label(window, font=("Ink Free", 35), bg="#0cc0e8")
    date_label.pack()


    thread1 = Thread(target=time_add, args=(time_label, day_label, date_label))
    thread1.daemon = True
    thread1.start()
    window.mainloop()
    

def time_add(time_label, day_label, date_label):
    try:
        while True:
            time_str = time.strftime("%I:%M:%S %p")
            time_label.config(text=time_str)

            day_str = time.strftime("%A")
            day_label.config(text=day_str)

            date_str = time.strftime("%B %d, %Y")
            date_label.config(text=date_str)

            time.sleep(1)
    except TclError:
        sys.exit()


if __name__ == "__main__":
    main()