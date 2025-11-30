# On the first line, you will receive an integer number representing the next pair of rows. On the next
# lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher
# than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
grades = {}
count = int(input())
student = ""
grade = 0.0
for turn in range(1, (count * 2) + 1):
    if turn % 2 != 0:
        student = input()
    else:
        grade = float(input())
    if turn % 2 == 0:
        if student not in grades:
            grades[student] = []
            grades[student].append(grade)
        else:
            grades[student].append(grade)


for student in list(grades.keys()):
    if sum(grades[student]) / len(grades[student]) < 4.50:
        del grades[student]

for student, grades in grades.items():
    print(f"{student} -> {sum(grades) / len(grades):.2f}")