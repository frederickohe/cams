import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import sqlite3
from PIL import Image, ImageTk
from scores import Scores

# Creating the variables
headlabelfont = ("Calibri", 15, "bold")
labelfont = ("Calibri", 14)
entryfont = ("Calibri", 14)


# Initializing the GUI window
main = Tk()
main.title("Score Manager")
main.geometry("1000x800")
main.resizable(0, 0)

# Creating the background and foreground color variables
lf_bg = "SteelBlue"  # bg color for the left_frame

# Creating the StringVar or IntVar variables
name_strvar = StringVar()
id_strvar = StringVar()
quiz_strvar = StringVar()
exercise_strvar = StringVar()
attendance_strvar = StringVar()

# Placing the components in the main window
Label(main, text="SCORE MANAGEMENT", font="Arial", bg=lf_bg).pack(side=TOP, fill=X)

left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=300, y=30, height=1000, width=380)


# Placing components in the left frame

Label(left_frame, text="Name *", font=labelfont, bg=lf_bg).place(x=30, y=10)
Entry(left_frame, width=20, textvariable=name_strvar, font=entryfont).place(x=170, y=10)

Label(left_frame, text="Stud ID *", font=labelfont, bg=lf_bg).place(x=30, y=50)
Entry(left_frame, width=20, textvariable=id_strvar, font=entryfont).place(x=170, y=50)
Label(left_frame, text="Date ", font=labelfont, bg=lf_bg).place(x=30, y=100)
doa = DateEntry(left_frame, font=("Arial", 12), width=15)
doa.place(x=170, y=100)

Label(left_frame, text="Quiz Score", font=labelfont, bg=lf_bg).place(x=30, y=150)
Entry(left_frame, width=20, textvariable=quiz_strvar, font=entryfont).place(
    x=170, y=150
)

Label(left_frame, text="Exercise Score", font=labelfont, bg=lf_bg).place(x=30, y=200)
Entry(left_frame, width=20, textvariable=exercise_strvar, font=entryfont).place(
    x=170, y=200
)

Label(left_frame, text="Attendance Score", font=labelfont, bg=lf_bg).place(x=30, y=250)
Entry(left_frame, width=20, textvariable=attendance_strvar, font=entryfont).place(
    x=170, y=250
)

from database import StudentDatabase


def send_scores():
    new_scores = Scores(
        name_strvar.get(),
        id_strvar.get(),
        doa.get(),
        quiz_strvar.get(),
        exercise_strvar.get(),
        attendance_strvar.get(),
    )

    # Example usage
    db = StudentDatabase("cams.db")

    # Add an assessment score
    db.add_assessment_score(new_scores)

    db.close()
def update_scores():
    # Retrieve the existing scores based on student ID and date
    student_id = id_strvar.get()
    assessment_date = doa.get()
    
    db = StudentDatabase("cams.db")
    existing_scores = db.get_scores_by_id_and_date(student_id, assessment_date)
    
    if existing_scores:
        # Update the scores
        existing_scores.quiz_score = quiz_strvar.get()
        existing_scores.exercise_score = exercise_strvar.get()
        existing_scores.attendance_score = attendance_strvar.get()

        # Save the updated scores
        db.update_scores(existing_scores)
        mb.showinfo("Update", "Scores updated successfully!")
    else:
        mb.showwarning("Update Error", "Scores not found for the specified ID and date")

    db.close()

    
def delete_scores():
    # Retrieve the existing scores based on student ID and date
    student_id = id_strvar.get()
    assessment_date = doa.get()

    db = StudentDatabase("cams.db")
    existing_scores = db.get_scores_by_id_and_date(student_id, assessment_date)

    if existing_scores:
        # Delete the scores
        db.delete_scores(existing_scores)
        mb.showinfo("Delete", "Scores deleted successfully!")
    else:
        mb.showwarning("Delete Error", "Scores not found for the specified ID and date")

    db.close()

    
def clear_fields():
    # Clear the values in the entry fields and date picker
    name_strvar.set("")
    id_strvar.set("")
    doa.set_date(datetime.date.today())  # Reset date to today
    quiz_strvar.set("")
    exercise_strvar.set("")
    attendance_strvar.set("")


# Place the buttons in the left frame

Button(left_frame, text="Add +", command=send_scores, font=labelfont, width=14).place(
    x=30, y=330
)
Button(left_frame, text="Update Scores", command=update_scores, font=labelfont, width=16).place(x=200, y=330)
Button(left_frame, text="Delete Scores", command=delete_scores, font=labelfont, width=14).place(x=30, y=420)
Button(left_frame, text="Clear", command=clear_fields, font=labelfont, width=14).place(x=200, y=420)


def home():
    # Close the current window
    main.destroy()


Button(main, text="Home", command=home, font=labelfont, width=12).place(x=20, y=750)

main.mainloop()
