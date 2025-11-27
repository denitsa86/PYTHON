# text = "programming basics"
# if " " in text:
#     new_text = text.replace(" ", "_")
#     print("Space found and replaced:", new_text)
# else:
#     print("No spaces found")
# You will be receiving names of students, their ID, and a course of programming they have taken
# in the format "{name}:{ID}:{course}". On the last line, you will receive the name of a course
# in snake case lowercase letters. You should print only the information of the students who have
# taken the corresponding course in the format: "{name} - {ID}" on separate lines.
course_dictionary = {}

# Read input until the last line (snake case course)
while True:
    data = input()
    if ":" not in data:  # last line is just the course name
        final_course = data
        break

    name, student_id, course = data.split(":")
    course = course.replace(" ", "_").lower()
    student_data = f"{name} - {student_id}"

    if course not in course_dictionary:
        course_dictionary[course] = []
    course_dictionary[course].append(student_data)

# Print only students for the final course
if final_course in course_dictionary:
    for student in course_dictionary[final_course]:
        print(student)
