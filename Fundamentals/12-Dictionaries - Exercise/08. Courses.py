# Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users.
# For each course, print the registered users.
# "{course_name} : {student_name}"   "-- {student_name}"
courses = {}
data = input().split(" : ")
while not data[0] == "end":
    course_name = data[0]
    student = data[1]
    if course_name not in courses:
        courses[course_name] = []
        courses[course_name].append(student)
    else:
        courses[course_name].append(student)

    data = input().split(" : ")
for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for item in value:
        print(f"-- {item}")
