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

# peach = Student("Peach", "Boyd", "PeachyKeen", 842)
# print(peach.slack_handle)

# for...in loop sets prop and value as variables for the properties and values on those properties in the Student object. It then loops through the peach object using __dict__ and .items(). __dict__ accesses all properties and values on an object. The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list. The view object will reflect any changes made to the dictionary. prop and value are assigned to the tuple pairs allowing us to put them in a print statement making them more readable.

# for prop, value in peach.__dict__.items():
#     print(f'{prop}: {value}\n')

# print(peach.__dict__)
