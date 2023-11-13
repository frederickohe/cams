import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import sqlite3
from PIL import Image, ImageTk

# Creating the variables
headlabelfont = ("Calibri", 15, "bold")
labelfont = ("Calibri", 14)
entryfont = ("Calibri", 14)

# Initializing the GUI window
main = Tk()
main.title("Student Management System")
main.geometry("1000x800")
main.resizable(0, 0)

# Creating the background and foreground color variables
lf_bg = "SteelBlue"  # bg color for the left_frame

# Creating the StringVar or IntVar variables

id_strvar = StringVar()
option_strvar = StringVar()

# Placing the components in the main window
Label(main, text="DATA RETRIEVAL", font="Arial", bg=lf_bg).pack(side=TOP, fill=X)
left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, height=1000, width=400)
right_frame = Frame(main, bg="white")
right_frame.place(x=400, y=30, height=1000, width=600)


# Placing components in the left frame

# Place the buttons in the left frame

Label(left_frame, text="Select Type", font=labelfont, bg=lf_bg).place(x=30, y=50)

Label(left_frame, text="Enter ID", font=labelfont, bg=lf_bg).place(x=30, y=150)

Entry(left_frame, width=20, textvariable=id_strvar, font=entryfont).place(x=170, y=150)

OptionMenu(left_frame, option_strvar, "Single", "All").place(x=170, y=50, width=110)

# Placing components in the right frame

Label(right_frame, text="Scores Records", font="Arial", bg=lf_bg, fg="Black").pack(
    side=TOP, fill=X
)


def retrieve_student():
    tree = ttk.Treeview(
        right_frame,
        height=100,
        selectmode=BROWSE,
        columns=(
            "Stud ID",
            "Name",
            "Contact No",
            "Email Addr",
            "Gender",
            "Date of Birth",
        ),
    )
    X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
    Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
    X_scroller.pack(side=BOTTOM, fill=X)
    Y_scroller.pack(side=RIGHT, fill=Y)

    tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)

    tree.heading("Stud ID", text="ID", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)
    tree.heading("Contact No", text="Contact No", anchor=CENTER)
    tree.heading("Email Addr", text="Email Addr", anchor=CENTER)
    tree.heading("Gender", text="Gender", anchor=CENTER)
    tree.heading("Date of Birth", text="DOB", anchor=CENTER)
    tree.column("#0", width=0, stretch=NO)
    tree.column("#1", width=80, stretch=NO)
    tree.column("#2", width=80, stretch=NO)
    tree.column("#3", width=80, stretch=NO)
    tree.column("#4", width=80, stretch=NO)
    tree.column("#5", width=80, stretch=NO)
    tree.place(y=30, relwidth=1, relheight=0.9, relx=0)

    type = option_strvar.get()
    option_id = id_strvar.get()

    conn = sqlite3.connect("cams.db")
    cursor = conn.cursor()

    # Clear the existing treeview data
    for item in tree.get_children():
        tree.delete(item)

    if type == "Single":
        # Retrieve a single record from the database (you need to modify this logic as needed)
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (option_id,))
        row = cursor.fetchone()
        if row:
            tree.insert("", "end", values=row)
    elif type == "All":
        # Retrieve all records from the database
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", "end", values=row)
    conn.commit()


def start_assessment():
    # First, create a new Treeview widget
    new_tree = ttk.Treeview(
        right_frame,
        height=100,
        selectmode=BROWSE,
        columns=(
            "Record ID",
            "Name",
            "Student ID",
            "Date of Submission",
            "Quiz Score",
            "Exercise Score",
            "Attendance Score",
        ),
    )
    X_scroller = Scrollbar(new_tree, orient=HORIZONTAL, command=new_tree.xview)
    Y_scroller = Scrollbar(new_tree, orient=VERTICAL, command=new_tree.yview)
    X_scroller.pack(side=BOTTOM, fill=X)
    Y_scroller.pack(side=RIGHT, fill=Y)

    new_tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)

    new_tree.heading("Record ID", text="Ass ID", anchor=CENTER)
    new_tree.heading("Name", text="Name", anchor=CENTER)
    new_tree.heading("Student ID", text="Stud ID", anchor=CENTER)
    new_tree.heading("Date of Submission", text="Submission Date", anchor=CENTER)
    new_tree.heading("Quiz Score", text="Quiz #", anchor=CENTER)
    new_tree.heading("Exercise Score", text="Exercise #", anchor=CENTER)
    new_tree.heading("Attendance Score", text="Attendance #", anchor=CENTER)
    new_tree.column("#0", width=0, stretch=NO)
    new_tree.column("#1", width=80, stretch=NO)
    new_tree.column("#2", width=80, stretch=NO)
    new_tree.column("#3", width=80, stretch=NO)
    new_tree.column("#4", width=80, stretch=NO)
    new_tree.column("#5", width=100, stretch=NO)
    new_tree.column("#6", width=100, stretch=NO)

    # Place the new_tree in the same position as the old tree
    new_tree.place(y=30, relwidth=1, relheight=0.9, relx=0)

    type = option_strvar.get()
    option_id = id_strvar.get()

    conn = sqlite3.connect("cams.db")
    cursor = conn.cursor()

    # Clear the existing treeview data
    # for item in new_tree.get_children():
    #     new_tree.delete(item)

    if type == "Single":
        # Retrieve a single assessment record from the database (modify as needed)
        cursor.execute(
            "SELECT * FROM assessment_scores WHERE student_id = ?", (option_id,)
        )
        rows = cursor.fetchall()
        for row in rows:
            new_tree.insert("", "end", values=row)
    elif type == "All":
        # Retrieve all assessment records from the database (modify as needed)
        cursor.execute("SELECT * FROM assessment_scores")
        rows = cursor.fetchall()
        for row in rows:
            new_tree.insert("", "end", values=row)
    conn.commit()


def home():
    # Close the current window
    main.destroy()
    # Import the new GUI file and create a new window
    import cams_app

    cams_app.main()


Button(main, text="Home", command=home, font=labelfont, width=12).place(x=20, y=750)
Button(
    left_frame,
    text="Retrieve Information",
    font=labelfont,
    command=retrieve_student,
    width=18,
).place(x=30, y=250)
Button(
    left_frame,
    text="Retrieve Assesment",
    command=start_assessment,
    font=labelfont,
    width=18,
).place(x=30, y=350)

main.update()
main.mainloop()

if __name__ == "__main__":
    main.update()
    main.mainloop()
