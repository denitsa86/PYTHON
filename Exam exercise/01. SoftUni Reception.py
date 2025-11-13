# Three employees are working on the reception all day. Each of them can handle a different number of students per hour. Your task is to calculate how much time it will take to answer all the questions of a given number of students.
# First, you will receive 3 lines with integers, representing the number of students that each employee can help per hour. On the following line, you will receive students count as a single integer.
# Every fourth hour, all employees have a break, so they don't work for an hour. It is the only break for the employees, because they don't need rest, nor have a personal life. Calculate the time needed to answer all the student's questions and print it in the following format: "Time needed: {time}h."
first_capacity = int(input())
second_capacity = int(input())
third_capacity = int(input())
total_capacity = first_capacity + second_capacity + third_capacity
total_students = int(input())
hours_counter = 0
while total_students > 0:
    hours_counter += 1
    if hours_counter % 4 == 0 and hours_counter > 0:
        continue
    else:
        total_students -= total_capacity
print(f"Time needed: {hours_counter}h.")