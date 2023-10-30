import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import sqlite3
from PIL import Image, ImageTk

# Creating the variables
headlabelfont = ("Calibri", 15, 'bold')
labelfont = ('Calibri', 14)
entryfont = ('Calibri', 14)

# Initializing the GUI window
main = Tk()
main.title('Student Management System')
main.geometry('1000x800')
main.resizable(0, 0)

# Load the JPG image from the "assets" folder using Pillow
image = Image.open("assets/back.jpg")
photo = ImageTk.PhotoImage(image)

# Create a Label widget with the image as the background
background_label = Label(main, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the entire main window

# Creating the background and foreground color variables
lf_bg = 'SteelBlue' # bg color for the main

# Creating the StringVar or IntVar variables
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
stream_strvar = StringVar()

# Placing components in the left frame

pic = Image.open("assets/other.jpg")
picture = ImageTk.PhotoImage(pic)

left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=210, y=80, height=367, width=612)

image_label = Label(left_frame, image=picture)
image_label.pack()

# Place the buttons in the left frame

Button(main, text='Manage Student', font=labelfont,  width=15).place(x=210, y=500)
Button(main, text='Manage Scores', font=labelfont,  width=15).place(x=210 + 230, y=500)
Button(main, text='Retrieve Data', font=labelfont,  width=15).place(x=210 + 460, y=500)

main.update()
main.mainloop()