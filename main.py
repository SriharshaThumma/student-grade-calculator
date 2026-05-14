from calculator import calculate_average, calculate_grade
from utils import get_marks

name = input("Enter student name: ")

marks = get_marks()

average = calculate_average(marks)

grade = calculate_grade(average)

print("\n----- RESULT -----")
print("Student:", name)
print("Average:", average)
print("Grade:", grade)