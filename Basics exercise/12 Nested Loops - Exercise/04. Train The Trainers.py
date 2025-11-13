#изчислява средната оценка от представянето на всяка една презентация от даден студент, а накрая -
# средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
#След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата
# "Student's final assessment is {среден успех от всички презентации}." и програмата приключва.
judges_count = int(input())
presentation = input()
presentation_count = 0
sum_total_grades = 0
sum_current_grades = 0
average_grade = 0
grades_counter = 0
while presentation != "Finish":
    sum_current_grades = 0
    for i in range(1, judges_count + 1):
        grade = input()
        sum_current_grades += float(grade)
        sum_total_grades += float(grade)
        grades_counter += 1
    presentation_count += 1
    average_grade = sum_current_grades / judges_count
    #total_average_grades += average_grade
    print(f"{presentation} - {average_grade:.2f}.")
    presentation = input()
print(f"Student's final assessment is {sum_total_grades / grades_counter:.2f}.")
