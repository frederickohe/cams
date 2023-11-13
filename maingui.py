import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import sqlite3
from PIL import Image, ImageTk

import subprocess

# Creating the variables
headlabelfont = ("Helvetica", 15, 'bold')
labelfont = ('Helvetica', 12)
entryfont = ('Helvetica', 14)

# Initializing the GUI window
interface = Tk()
interface.title('Student Management System')
interface.geometry('1000x800')
interface.resizable(0, 0)

# Load the JPG image from the "assets" folder using Pillow
image = Image.open("assets/back.jpg")
photo = ImageTk.PhotoImage(image)

# Create a Label widget with the image as the background
background_label = Label(interface, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the entire interface window

# Creating the background and foreground color variables
lf_bg = 'SteelBlue' # bg color for the interface

# Function to open a new GUI window
def open_manage_student():
    subprocess.call(['python', 'stdntgui.py'])
    
def open_manage_scores():
    subprocess.call(['python', 'scoresgui.py'])

def open_retrieve_data():
    subprocess.call(['python', 'retrievegui.py'])

# Placing components in the left frame

pic = Image.open("assets/other.jpg")
picture = ImageTk.PhotoImage(pic)

left_frame = Frame(interface, bg=lf_bg)
left_frame.place(x=210, y=80, height=367, width=612)

image_label = Label(left_frame, image=picture)
image_label.pack()

# Create the buttons
Button(interface, text='Manage Student', font=labelfont, width=15, command=open_manage_student).place(x=210, y=500)
Button(interface, text='Manage Scores', font=labelfont, width=15, command=open_manage_scores).place(x=210 + 230, y=500)
Button(interface, text='Retrieve Data', font=labelfont, width=15, command=open_retrieve_data).place(x=210 + 460, y=500)

interface.mainloop()
