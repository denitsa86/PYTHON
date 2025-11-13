# Напишете програма, която отпечатва класа на животното според неговото име,
# въведено от потребителя.
# 1.	dog -> mammal
# 2.	crocodile, tortoise, snake -> reptile
# 3.	others -> unknown
animal = input()
match animal:
    case "dog":
        print("mammal")
    case "crocodile" | "tortoise" | "snake":
        print("reptile")
    case _:
        print("unknown")
