import sqlite3


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/clb/workspace/python/student-exercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
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
            for student in all_students:
                print(f'{student[1]} {student[2]} is in {student[5]}')

reports = StudentExerciseReports()
reports.all_students()