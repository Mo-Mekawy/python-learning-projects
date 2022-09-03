from tkinter import *



equation_text = ""
equation_var = None
def main():
    window = Tk()
    window.title("Mohamed's Calculator")
    window.geometry("500x500")
    window.resizable(width=False, height=False)
    window.config(bg="limegreen")

    global equation_var
    equation_var = StringVar()
    label = Label(
        window,
        textvariable=equation_var,
        font=("Arial", 20),
        bg="white",
        width=24,
        height=2,
        padx=3,
    )
    label.place(x=50, y=10)

    frame = Frame(window, width=405, height=450)
    frame.place(x=50, y=100)

    # first row buttons
    button7 = Button(frame, text="7", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press(7))
    button7.grid(row=0, column=0)

    button8 = Button(frame, text="8", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press(8))
    button8.grid(row=0, column=1)

    button9 = Button(frame, text="9", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press(9))
    button9.grid(row=0, column=2)

    button_plus = Button(frame, text="+", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press("+"))
    button_plus.grid(row=0, column=3)
    '''----------------------------------------------------------------------------------------------------------------'''
    # second row buttons
    button4 = Button(frame, text="4", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press(4))
    button4.grid(row=1, column=0)

    button5 = Button(frame, text="5", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press(5))
    button5.grid(row=1, column=1)

    button6 = Button(frame, text="6", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press(6))
    button6.grid(row=1, column=2)

    button_minus = Button(frame, text="-", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press("-"))
    button_minus.grid(row=1, column=3)
    '''----------------------------------------------------------------------------------------------------------------'''
    # third row buttons
    button1 = Button(frame, text="1", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press(1))
    button1.grid(row=2, column=0)

    button2 = Button(frame, text="2", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press(2))
    button2.grid(row=2, column=1)

    button3 = Button(frame, text="3", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press(3))
    button3.grid(row=2, column=2)
    
    button_multi = Button(frame, text="*", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press("*"))
    button_multi.grid(row=2, column=3)

    # forth row buttons
    button0 = Button(frame, text="0", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press(0))
    button0.grid(row=3, column=0)

    button_dot = Button(frame, text=".", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press('.'))
    button_dot.grid(row=3, column=1)

    button_equal = Button(frame, text="=", padx=5, height=4, width=9, font=("Arial", 12), command =equals)
    button_equal.grid(row=3, column=2)

    button_div = Button(frame, text="/", padx=5, height=4, width=9, font=("Arial", 12), command =lambda : button_press("/"))
    button_div.grid(row=3, column=3)

    # clear button
    button_clear = Button(window, text="Clear", padx=5, height=2, width=42, font=("Arial", 12), command=clear)
    button_clear.place(x=50, y=445)

    window.mainloop()


def button_press(num):
    global equation_text
    global equation_var

    equation_text += str(num)
    equation_var.set(equation_text)


def equals():
    global equation_text
    global equation_var

    try:
        total = str(eval(equation_text))
    except ZeroDivisionError:
        equation_var.set("cannot divide by zero")
        equation_text = ("")
    except SyntaxError:
        equation_var.set("Syntax Error")
        equation_text = ("")
    else:
        equation_var.set(total)
        equation_text = total


def clear():
    global equation_text
    global equation_var

    equation_var.set("")
    equation_text = ("")


if __name__ == "__main__":
    main()
