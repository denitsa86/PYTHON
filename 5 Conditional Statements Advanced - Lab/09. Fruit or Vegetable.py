#чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.
# fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper
# и carrot;
# •	Всички останали са "unknown".
from unittest import case

product = input()
match product :
    case "banana" | "apple" | "kiwi" | "cherry" | "lemon" | "grapes":
        print("fruit")
    case "tomato" | "cucumber" |"pepper" | "carrot":
        print("vegetable")
    case _:
        print("unknown")
