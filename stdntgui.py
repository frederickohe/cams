import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import sqlite3
from PIL import Image, ImageTk
from student import Student
from database import StudentDatabase

# Creating the variables
headlabelfont = ("Calibri", 15, "bold")
labelfont = ("Calibri", 14)
entryfont = ("Calibri", 14)

interface = Tk()

# Initializing the GUI window

interface.title("Student Manager")
interface.geometry("1000x800")
interface.resizable(0, 0)

# Creating the StringVar or IntVar variables
name_strvar = StringVar()
contact_strvar = StringVar()
email_strvar = StringVar()
gender_strvar = StringVar()
deleteid_strvar = StringVar()
dob = None

# Creating the background and foreground color variables
lf_bg = "SteelBlue"  # bg color for the left_frame

# Placing the components in the interface window
Label(interface, text="STUDENT MANAGEMENT", font="Arial", bg=lf_bg).pack(
    side=TOP, fill=X
)

left_frame = Frame(interface, bg=lf_bg)
left_frame.place(x=300, y=30, height=1000, width=400)


def send_student():
    new_student = Student(
        name_strvar.get(),
        contact_strvar.get(),
        email_strvar.get(),
        gender_strvar.get(),
        dob.get(),
    )

    # Example usage
    db = StudentDatabase("cams.db")

    # Add a new student
    db.add_student(new_student)

    db.close()


def clear_fields():
    # Clearing the data in the StringVar and DateEntry
    name_strvar.set("")
    contact_strvar.set("")
    email_strvar.set("")
    gender_strvar.set("")
    deleteid - strvar.set("")
    dob.set_date(datetime.date.today())  # Set the DateEntry to the current date


def delete_record():
    try:
        db = StudentDatabase("cams.db")
        student_id_to_delete = int(deleteid_strvar.get())
        db.delete_student(student_id_to_delete)
        mb.showinfo("Success", "Record deleted successfully!")
        db.close()
    except ValueError:
        mb.showerror("Error", "Please enter a valid Student ID")

def home():
    # Close the current window
    interface.destroy()


# Placing components in the left frame
Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(x=30, y=50)
Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(x=30, y=100)
Label(left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(x=30, y=150)
Label(left_frame, text="Gender", font=labelfont, bg=lf_bg).place(x=30, y=200)
Label(left_frame, text="Birth Date(DOB)", font=labelfont, bg=lf_bg).place(x=30, y=250)
Label(left_frame, text="Student ID", font=labelfont, bg=lf_bg).place(x=30, y=300)
Label(left_frame, text="Enter ID To Delete", font=labelfont, bg=lf_bg).place(
    x=30, y=480
)


Entry(left_frame, width=20, textvariable=name_strvar, font=entryfont).place(x=170, y=50)
Entry(left_frame, width=19, textvariable=contact_strvar, font=entryfont).place(
    x=170, y=100
)
Entry(left_frame, width=19, textvariable=email_strvar, font=entryfont).place(
    x=170, y=150
)

Entry(left_frame, width=16, textvariable=deleteid_strvar, font=entryfont).place(
    x=210, y=480
)

Label(left_frame, text="Auto Generated", font="Arial", bg="white").place(x=170, y=300)

OptionMenu(left_frame, gender_strvar, "Male", "Female").place(x=170, y=200, width=70)

dob = DateEntry(left_frame, font=("Arial", 12), width=15)
dob.place(x=170, y=250)

Button(
    left_frame, text="Add New Student", command=send_student, font=labelfont, width=16
).place(x=30, y=380)

Button(interface, text="Home", command=home, font=labelfont, width=12).place(
    x=20, y=750
)

Button(
    left_frame, text="Delete Record", command=delete_record, font=labelfont, width=15
).place(x=30, y=550)

Button(
    left_frame, text="Clear Fields", command=clear_fields, font=labelfont, width=15
).place(x=215, y=380)

interface.mainloop()
