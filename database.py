import sqlite3

class StudentDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Create tables if they don't exist
        self.create_tables()

    def create_tables(self):
        # Create a table for students
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                contact TEXT,
                email TEXT,
                gender TEXT,
                dob DATE
            )
        ''')

        # Create a table for assessment scores
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS assessment_scores (
                 assessment_id INTEGER PRIMARY KEY,
                 name TEXT,
                 student_id INTEGER,
                 date DATE,
                 quiz_score INTEGER,
                 exercise_score INTEGER,
                 attendance_score INTEGER,
                 FOREIGN KEY (student_id) REFERENCES students (student_id)
             )
        ''')

        self.conn.commit()

    def add_student(self, object):
        # Add a new student to the database
        self.cursor.execute('''
            INSERT INTO students (name, contact, email, gender, dob)
            VALUES (?, ?, ?, ?, ?)
        ''', (object.name, object.contact, object.email, object.gender, object.dob))
        self.conn.commit()

    def add_assessment_score(self, object):
        # Add assessment scores for a student
        self.cursor.execute('''
            INSERT INTO assessment_scores (name, student_id, date, quiz_score, exercise_score, attendance_score)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (object.name, object.student_id, object.date, object.quiz_score, object.exercise_score, object.attendance_score))
        self.conn.commit()
        
    def delete_student(self, student_id):
        # Delete a student from the database based on their ID
        self.cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        self.conn.commit()
        
    def get_scores_by_id_and_date(self, student_id, assessment_date):
        # Retrieve scores based on student ID and assessment date
        self.cursor.execute('''
            SELECT * FROM assessment_scores
            WHERE student_id = ? AND date = ?
        ''', (student_id, assessment_date))

        row = self.cursor.fetchone()

        if row:
            # Create a Scores object and return it
            scores = Scores(row[1], row[2], row[3], row[4], row[5], row[6])
            return scores
        else:
            return None

    def delete_scores(self, scores_object):
        # Delete scores based on the provided Scores object
        self.cursor.execute('''
            DELETE FROM assessment_scores
            WHERE student_id = ? AND date = ?
        ''', (scores_object.student_id, scores_object.date))
        self.conn.commit()

    # You can implement more methods for updating, deleting, and retrieving data as needed.

    def close(self):
        # Close the database connection
        self.conn.close()

