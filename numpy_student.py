import csv
import numpy as np

marks = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks.append([
            int(row["python"]),
            int(row["sql"]),
            int(row["docker"])
        ])

print(marks)

import numpy as np

marks_array = np.array(marks)

print("NumPy Array:")
print(marks_array)

print("Type:", type(marks_array))

#axis=0 → column-wise

subject_mean = np.mean(marks_array, axis=0)

student_means = np.mean(marks_array, axis=1)

print("Student Means:")
print(student_means)