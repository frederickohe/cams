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
main.title('Student Manager')
main.geometry('1000x800')
main.resizable(0, 0)

# Creating the background and foreground color variables
lf_bg = 'SteelBlue' # bg color for the left_frame

# Creating the StringVar or IntVar variables
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
studid_strvar = StringVar()

# Placing the components in the main window
Label(main, text="STUDENT MANAGEMENT", font='Arial', bg=lf_bg).pack(side=TOP, fill=X)

left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=300, y=30, height=1000, width=400)


# Placing components in the left frame
Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(x=30, y=50)
Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(x=30,y=100)
Label(left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(x=30,y=150)
Label(left_frame, text="Gender", font=labelfont, bg=lf_bg).place(x=30, y=200)
Label(left_frame, text="Birth Date(DOB)", font=labelfont, bg=lf_bg).place(x=30, y=250)
Label(left_frame, text="Student ID", font=labelfont, bg=lf_bg).place(x=30, y=300)
Entry(left_frame, width=20, textvariable=name_strvar, font=entryfont).place(x=170, y=50)
Entry(left_frame, width=19, textvariable=contact_strvar, font=entryfont).place(x=170, y=100)
Entry(left_frame, width=19, textvariable=email_strvar, font=entryfont).place(x=170,y=150)
Entry(left_frame, width=19, textvariable=studid_strvar, font=entryfont).place(x=170, y=300)
OptionMenu(left_frame, gender_strvar, 'Male', "Female").place(x=170, y=200, width=70)
dob = DateEntry(left_frame, font=("Arial", 12), width=15)
dob.place(x=170, y=250)

Button(left_frame, text='Add New Student', font=labelfont, width=18).place(x=100, y=380)

#Place the buttons in the left frame

Button(left_frame, text='Delete Record', font=labelfont, width=15).place(x=30, y=450)
Button(left_frame, text='Clear Fields', font=labelfont,  width=15).place(x=215, y=450)


# Placing components in the right frame


#display_records()


main.update()
main.mainloop()