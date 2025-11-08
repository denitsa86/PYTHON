#програма, която да изчислява процента на билетите за всеки тип от продадените билети: студентски(student),
# стандартен(standard) и детски(kid), за всички прожекции. Трябва да изчислите и колко процента от
# залата е запълнена за всяка една прожекция.
# •	На първия ред до получаване на командата "Finish" - име на филма – текст
# •	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# •	За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на
# командата "End": o	Типа на закупения билет - текст ("student", "standard", "kid")
# •	След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full."
# •	При получаване на командата "Finish" да се отпечатат четири реда:
standard_tickets = 0
student_tickets = 0
kid_tickets = 0
current_total_tickets = 0
total_tickets_sold = 0
movie = input()
while movie != "Finish":
    capacity = int(input())
    free_seats = capacity
    #total_tickets = 0
    ticket_type = input()
    while ticket_type != "End" and ticket_type != "Finish" and free_seats > 0:
        for i in range(1, capacity +1):
            if free_seats <= 0 or ticket_type == "End" or ticket_type == "Finish":
                break
            match ticket_type:
                case "standard":
                    standard_tickets += 1
                case "student":
                    student_tickets += 1
                case "kid":
                    kid_tickets += 1
            current_total_tickets += 1
            total_tickets_sold += 1
            free_seats -= 1
            if free_seats == 0:
                break
            ticket_type = input()
    if ticket_type == "End" or ticket_type == "Finish" or free_seats <= 0:
        if ticket_type == "Finish":
            movie = "Finish"
            break
        print(f"{movie} - {((current_total_tickets / capacity) * 100):.2f}% full.")
        current_total_tickets = 0
        movie = input()

print(f"Total tickets: {total_tickets_sold}")
print(f"{(student_tickets / total_tickets_sold * 100):.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets_sold * 100):.2f}% standard tickets.")
print(f"{(kid_tickets / total_tickets_sold * 100):.2f}% kids tickets.")



