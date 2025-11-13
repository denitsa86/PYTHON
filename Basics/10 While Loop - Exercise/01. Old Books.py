# въвежда търсената от нея книга (текст). Докато Ани не намери любимата си книга или не провери всички
# книги в библиотеката, програмата трябва да чете всеки път на нов ред името на всяка следваща книга
# (текст), която тя проверява. Книгите в библиотеката са свършили щом получите текст "No More Books".
# •	Ако не открие търсената книгата да се отпечата на два реда:
# o	"The book you search is not here!"
# o	"You checked {брой} books."
# •	Ако открие книгата си се отпечатва един ред:
# o	"You checked {брой} books and found it."
desired_book = input()
text = input()
counter = 0
while text != "No More Books":
    if text == desired_book :
        print(f"You checked {counter} books and found it.")
        break
    else:
        counter += 1
        text = input()
if text == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {counter} books.")


