"""
You must define a custom type for representing a student in code. A student can only be in one cohort at a time. A student can be working on many exercises at a time.

Properties
First name
Last name
Slack handle
The student's cohort
The collection of exercises that the student is currently working on
"""

# Student class with positional arguments for first_name, last_name, slack_handle and cohort. Exercises are set as an empty list. 
class Student:
    def __init__(self, first_name, last_name, slack_handle, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.exercises = []

peach = Student("Peach", "Boyd", "PeachyKeen", 842)
print(peach.slack_handle)
