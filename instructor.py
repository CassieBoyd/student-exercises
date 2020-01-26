from nssperson import NSSPerson

"""
You must define a type for representing an instructor in code.

First name
Last name
Slack handle
The instructor's cohort
The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
A method to assign an exercise to a student
"""

class Instructor(NSSPerson):
    def __init__ (self, first_name,last_name, slack_handle, cohort, specialty):
        super().__init__(first_name, last_name, cohort, slack_handle)
        self.specialty = specialty

# Method on Instructor object takes student and new_exercise as positional arguments to append the exercises property on a student instance with a new_exercise
    def assign_exercise (self, student, new_exercise):
        student.exercises.append(new_exercise)