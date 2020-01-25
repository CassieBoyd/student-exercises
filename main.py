from exercise import Exercise
from cohort import Cohort
from student import Student
from instructor import Instructor

"""
Once you have defined all of your custom types, go to main.py, import the classes you need, and implement the following logic.

Create 4, or more, exercises.
Create 3, or more, cohorts.
Create 4, or more, students and assign them to one of the cohorts.
Create 3, or more, instructors and assign them to one of the cohorts.
Have each instructor assign 2 exercises to each of the students.
"""

# Creating exercises
paint_the_fence = Exercise("Paint The Fence","JavaScript")
sand_the_floor = Exercise("Sand The Floor", "JavaScript")
paint_the_house = Exercise("Paint The House", "JavaScript")
wax_on = Exercise("Wax On", "Python")
wax_off = Exercise("Wax Off", "Python")

# Creating cohorts
day_cohort_98 = Cohort("Day Cohort 98")
cobra_kai = Cohort("Night Cohort Cobra Kai")
miyagi_dojo = Cohort("Day Cohort Miyagi Dojo")

# Creating students and assigning them to cohorts with .append()
daniel_larusso = Student("Daniel", "LaRusso", "Daniel-san", "Day Cohort Miyagi Dojo")
miyagi_dojo.students.append(daniel_larusso)
johhny_lawrence = Student("Johnny", "Lawrence", "L3g5w33p3r", "Night Cohort Cobra Kai")
cobra_kai.students.append(johhny_lawrence)
john_doe = Student("John", "Doe", "DoeBoi", "Day Cohort 98")
day_cohort_98.students.append(john_doe)
janet_doe = Student("Janet", "Doe", "DammitJanet", "Day Cohort 98")
day_cohort_98.students.append(janet_doe)

# Checking that students are in their cohorts
# print(cobra_kai.students[0].first_name)
# print(miyagi_dojo.students[0].first_name)
# print(day_cohort_98.students[0].first_name)
# print(day_cohort_98.students[1].first_name)


# Creating instructors
nariyoshi_miyagi = Instructor("Nariyoshi", "Miyagi", "Mr.Miyagi", "Day Cohort Miyagi Dojo", "Crane Kick")

john_kreese = Instructor("John", "Kreese", "NoMercy", "Night Cohort Cobra Kai", "Sweep The Leg")

frank_n_furter = Instructor("Frank", "Furter","Sw3377ransv3s7173", "Day Cohort 98", "The Time Warp")

# Instructors assigning exercises 
nariyoshi_miyagi.assign_exercise(daniel_larusso, paint_the_fence)
nariyoshi_miyagi.assign_exercise(daniel_larusso, paint_the_house)
print("Daniel,", daniel_larusso.exercises[0].name)
print("Daniel,", daniel_larusso.exercises[1].name)

john_kreese.assign_exercise(johhny_lawrence, wax_on)
john_kreese.assign_exercise(johhny_lawrence, wax_off)
print("Johnny,", johhny_lawrence.exercises[0].name)
print("Johnny,", johhny_lawrence.exercises[1].name)


for student in day_cohort_98.students:
    frank_n_furter.assign_exercise(student, wax_on)
    frank_n_furter.assign_exercise(student, sand_the_floor)

for exercise in janet_doe.exercises:
    print("Janet,", exercise.name)

for exercise in john_doe.exercises:
    print("John,", exercise.name)