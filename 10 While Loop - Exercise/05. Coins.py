#възможно най-малко монети ресто. Напишете програма, която приема сума - рестото, което трябва да се
# върне и изчислява с колко най-малко монети може да стане това.
#convert = change * 100;
change = float(input())
cents = int(change * 100)
coin_counter = 0
while cents > 0:
    if cents - 200 >= 0:
        coin_counter += 1
        cents -= 200
    elif cents - 100 >= 0:
        coin_counter += 1
        cents -= 100
    elif cents - 50 >= 0:
        coin_counter += 1
        cents -= 50
    elif cents - 20 >= 0:
        coin_counter += 1
        cents -= 20
    elif cents - 10 >= 0:
        coin_counter += 1
        cents -= 10
    elif cents - 5 >= 0:
        coin_counter += 1
        cents -= 5
    elif cents - 2 >= 0:
        coin_counter += 1
        cents -= 2
    elif cents - 1 >= 0:
        coin_counter += 1
        cents -= 1
print(coin_counter)
