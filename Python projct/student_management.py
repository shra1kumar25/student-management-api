name = "Sravan"
age = 30

print("Name:", name)
print("Age:", age)

student_age = 30
student_marks = 75.5

print(student_age)
print(type(student_age))

print(student_marks)
print(type(student_marks))

subjects = ["Python", "SQL", "Docker"]

print(subjects)
print(type(subjects))

print(subjects[0])
print(subjects[1])
print(subjects[2])

subjects = ["Python", "SQL", "Docker"]

print(subjects)
subjects.append("Pandas")

print(subjects)

subjects.remove("SQL")

print(subjects)

student_location = ("Hyderabad", "India")

print(student_location)
print(type(student_location))

#access the tuple values using index

student_location = ("Hyderabad", "India")

print(student_location)
print(type(student_location))

print(student_location[0])
print(student_location[1])

#Dictionary

student = {
    "name": "Sravan",
    "age": 30,
    "course": "Python"
}

print(student)
print(type(student))










student_name = "Sravan Kumar"
student_email = "sravan@example.com"
student_course = "Python"
student_department = "Computer Science"
student_city = "Hyderabad"
student_status = "Active"

print(student_name)
print(student_email)
print(student_course)
print(student_department)
print(student_city)
print(student_status)











#string

print(student_name.upper())
print(student_name.lower())
print(student_name.title())

print(student_email.endswith("@example.com"))
print(student_course.startswith("Py"))

print(len(student_name))


#numbers

student_age = 30
student_marks = 85.5
student_attendance = 92.5
student_projects = 4
student_experience = 2.5













#Dictionary

student = {
    "id": 101,
    "name": "Sravan Kumar",
    "age": 30,
    "email": "sravan@example.com",
    "course": "Python",
    "department": "Computer Science",
    "city": "Hyderabad",
    "marks": 85.5,
    "attendance": 92.5,
    "status": "Active"
}



#datatype_student.py

student_name = 'Kiran'
student_age = 26
student_percentage = 55.5
student_active = True
student_phone = "9989998989"

print(student_name, type(student_name))
print(student_age, type(student_age))
print(student_percentage, type(student_percentage))
print(student_active, type(student_active))
print(student_phone, type(student_phone))


#list

subjects = [
    "Python",
    "SQL",
    "Docker",
    "Git",
    "Linux"
]


marks = [45, 78, 92, 56, 88, 34, 95, 67, 81, 73]

for mark in marks:
    print(mark)

#average marks:-

marks = [45, 78, 92, 56, 88, 34, 95, 67, 81, 73]

print("Marks:")

for mark in marks:
    print(mark)

total = sum(marks)
print("Total:", total)

average = sum(marks) / len(marks)
print("Average:", average)

print("Highest:", max(marks))
print("Lowest:", min(marks))

#Pass / Fail / Distinction

marks = [45, 78, 92, 56, 88, 34, 95, 67, 81, 73]

print("\nPass/Fail:")

for mark in marks:
    if mark >= 40:
        print(mark, "PASS")
    else:
        print(mark, "FAIL")


        #if else if
    
    
for mark in marks:
    if mark >= 90:
        print(mark, "A+")
    elif mark >= 80:
        print(mark, "A")
    elif mark >= 70:
        print(mark, "B")
    elif mark >= 60:
        print(mark, "C")
    elif mark >= 40:
        print(mark, "D")
    else:
        print(mark, "F")




def welcome_student(name):
    print("Welcome", name)


welcome_student("Sravan")
welcome_student("Kiran")
welcome_student("Ramesh")

#function with Multiple parameters:-

def student_details(name, age, course)
print("Sravan,30,python")
print("Kiran,26,sql")
print("Ramesh,25,devops")