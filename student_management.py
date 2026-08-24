def calculate_total(python_marks, sql_marks, docker_marks):
    return python_marks + sql_marks + docker_marks


def calculate_average(python_marks, sql_marks, docker_marks):
    total = python_marks + sql_marks + docker_marks
    return total / 3


sravan_total = calculate_total(90, 85, 88)
kiran_total = calculate_total(78, 92, 85)
ramesh_total = calculate_total(88, 76, 91)

print("Sravan Total:", sravan_total)
print("Kiran Total:", kiran_total)
print("Ramesh Total:", ramesh_total)


sravan_average = calculate_average(90, 85, 88)
kiran_average = calculate_average(78, 92, 85)
ramesh_average = calculate_average(88, 76, 91)

print("Sravan Average:", round(sravan_average, 2))
print("Kiran Average:", round(kiran_average, 2))
print("Ramesh Average:", round(ramesh_average, 2))


def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def student_report(name, python_marks, sql_marks, docker_marks):
    total = calculate_total(python_marks, sql_marks, docker_marks)
    average = calculate_average(python_marks, sql_marks, docker_marks)
    grade = get_grade(average)

    print("Student:", name)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)

sravan_marks = [90, 85, 88]
kiran_marks = [78, 92, 85]
ramesh_marks = [88, 76, 91]

print("Sravan Total:", calculate_total(sravan_marks))
print("Kiran Total:", calculate_total(kiran_marks))
print("Ramesh Total:", calculate_total(ramesh_marks))


def calculate_total(marks):
    return sum(marks)


sravan_marks = [90, 85, 88]
kiran_marks = [78, 92, 85]
ramesh_marks = [88, 76, 91]

def calculate_total(marks):
    return sum(marks)


sravan_marks = [90, 85, 88]
kiran_marks = [78, 92, 85]
ramesh_marks = [88, 76, 91]


print("Sravan Total:", calculate_total(sravan_marks))
print("Kiran Total:", calculate_total(kiran_marks))
print("Ramesh Total:", calculate_total(ramesh_marks))
print("Sravan Total:", calculate_total(sravan_marks))
print("Kiran Total:", calculate_total(kiran_marks))
print("Ramesh Total:", calculate_total(ramesh_marks))