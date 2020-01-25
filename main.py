from exercise import Exercise
from cohort import Cohort
from student import Student

"""
Once you have defined all of your custom types, go to main.py, import the classes you need, and implement the following logic.

Create 4, or more, exercises.
Create 3, or more, cohorts.
Create 4, or more, students and assign them to one of the cohorts.
Create 3, or more, instructors and assign them to one of the cohorts.
Have each instructor assign 2 exercises to each of the students.
"""

paint_the_fence = Exercise("Paint The Fence","JavaScript")
sand_the_floor = Exercise("Sand The Floor", "JavaScript")
wax_on = Exercise("Wax On", "Python")
wax_off = Exercise("Wax Off", "Python")

day_cohort_98 = Cohort("Day Cohort 98")
cobra_kai = Cohort("Night Cohort Cobra Kai")
miyagi_dojo = Cohort("Day Cohort Miyagi Dojo")

daniel_larusso = Student("Daniel", "LaRusso", "Daniel-san", "Day Cohort Miyagi Dojo")
miyagi_dojo.students.append(daniel_larusso)
johhny_lawrence = Student("Johnny", "Lawrence", "Kn335w33p3r", "Night Cohort Cobra Kai")
cobra_kai.students.append(johhny_lawrence)
john_doe = Student("John", "Doe", "DoeBoi", "Day Cohort 98")
day_cohort_98.students.append(john_doe)
janet_doe = Student("Janet", "Doe", "DammitJanet", "Day Cohort 98")
day_cohort_98.students.append(janet_doe)

print(cobra_kai.students[0].first_name)
