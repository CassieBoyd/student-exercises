from nssperson import NSSPerson
"""
You must define a custom type for representing a student in code. A student can only be in one cohort at a time. A student can be working on many exercises at a time.

Properties
First name
Last name
Slack handle
The student's cohort
The collection of exercises that the student is currently working on
"""

# Now you have a simple class that you can use to generate a new object, with contextual properties, for interacting with student data. You would create a new instance like so.

# student = Student('Bart', 'Simpson', '@bart', 'Cohort 8')
# print(f'{student.first_name} {student.last_name} is in {student.cohort}')

# Output
# > "Bart Simpson is in Cohort 8"
# class Student():

#     def __init__(self, first, last, handle, cohort):
#         self.first_name = first
#         self.last_name = last
#         self.slack_handle = handle
#         self.cohort = cohort


# Student class with positional arguments for first_name, last_name, slack_handle and cohort. Exercises are set as an empty list. 
class Student(NSSPerson):
    def __init__(self, first_name, last_name, slack_handle, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.exercises = []
    # def __str__(self):
    #     return f'{self.first_name} {self.last_name} is in {self.cohort}'

# Provides a default string representation of a student.
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'

# peach = Student("Peach", "Boyd", "PeachyKeen", 842)
# print(peach.slack_handle)

# for...in loop sets prop and value as variables for the properties and values on those properties in the Student object. It then loops through the peach object using __dict__ and .items(). __dict__ accesses all properties and values on an object and returns them as a dictionary. The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list. The view object will reflect any changes made to the dictionary. prop and value are assigned to the tuple pairs allowing us to put them in a print statement making them more readable.

# for prop, value in peach.__dict__.items():
#     print(f'{prop}: {value}\n')

# print(peach.__dict__)
# print("\n\n")
# peach_dict = peach.__dict__
# for key in peach_dict:
#     print(key, peach_dict[key])
# print("\n\n")
# for key, value in peach_dict.items():
    # ("first_name", "Peach")
    # print(key, value)

if __name__ == "__main__":
    print("Student is running as Main")