from tkinter import *
import time
from PIL import ImageTk, Image
import sys


bg_photo = Image.open(r"F:\mohamed files\images\Earth2.jpeg")
WIDTH, HEIGHT = bg_photo.size

x_speed = 2
y_speed = 3

window = Tk()
window.resizable(width=False, height=False)

photoimage = PhotoImage(file=r"F:\mohamed files\images\ufo.png")
bg = ImageTk.PhotoImage(bg_photo)

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
canvas.pack()
bg_image = canvas.create_image(0, 0, image=bg, anchor=NW)
image = canvas.create_image(0, 0, image=photoimage, anchor=NW)

image_width = photoimage.width()
image_height = photoimage.height()
try:
    while True:
        coordinates = canvas.coords(image)
        if coordinates[0] > WIDTH - image_width or coordinates[0] < 0:
            x_speed *= -1
        if coordinates[1] > HEIGHT - image_height or coordinates[1] < 0:
            y_speed *= -1

        canvas.move(image, x_speed, y_speed)
        window.update()
        time.sleep(0.01)

except TclError:
    sys.exit()
