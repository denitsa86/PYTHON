#You will receive a single number n. On the next n lines you will receive names of courses. You have to
# create a list of them and print it
number = int(input())
courses = []
for i in range(number):
    course = input()
    courses.append(course)
print(courses)