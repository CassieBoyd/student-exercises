import sqlite3
from student import Student
from cohort import Cohort

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/clb/workspace/python/student-exercises/studentexercises.db"

    # The sqlite3 package has a row_factory property on the connection object where you can specify the instructions for the conversion of row of data -> Student instance with your own function.

# The function assigned to the row_factory property must take two arguments - the cursor, and the current row of data. It must return something. In this case, it will return a new instance of student.
    # def create_student(self, cursor, row):
    #     return Student(row[1], row[2], row[3], row[5])

    # lambda cursor, row: Student(row[1], row[2], row[3], row[5])

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            from Student s
            join Cohort c on s.cohort_id = c.Id
            order by s.cohort_id
            """)

# When you instruct the sqlite3 package to fetchall() in the code below, it takes your SQL string and walks over to the database and executes it. It then takes all of the rows that the database generates, and creates a tuple out of each one. It then puts all of those tuples into a list.
            all_students = db_cursor.fetchall()

# Since a tuple is simply an immutable list, you can use square-bracket notation to extract individual items out of it. Displaying a tuple to the terminal as output is not good UX. Use the following code to just display the first name (second column), last name (third column), and cohort name (sixth column).
            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

# Now when you run the fetchall() method, you will end up with a list of Student objects instead of a list of tuples. This means that you can access those properties when displaying them.
            for student in all_students:
                print(student)
            
def all_cohorts(self):

        """Retrieve all cohort names"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            from Student s
            join Cohort c on s.cohort_id = c.Id
            order by s.cohort_id
            """)
            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)

reports = StudentExerciseReports()
reports.all_students()