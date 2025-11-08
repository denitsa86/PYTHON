fails_limit = int(input())
failed_times = 0
solved_problems_count = 0
grades_sum = 0
last_problem = ""
has_failed = True
while failed_times < fails_limit:
    problem = input()
    if problem == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problems_count += 1
    last_problem = problem
# •	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# o	"Average score: {средна оценка}"
# o	"Number of problems: {броя на всички задачи}"
# o	"Last problem: {името на последната задача}"
# •	Ако получи определеният брой незадоволителни оценки:
# o	"You need a break, {брой незадоволителни оценки} poor grades."
if has_failed:
    print(f"You need a break, {failed_times} poor grades.")
else:
    print(f"Average score: {(grades_sum / solved_problems_count):.2f}")
    print(f"Number of problems: {solved_problems_count}")
    print(f"Last problem: {last_problem}")
