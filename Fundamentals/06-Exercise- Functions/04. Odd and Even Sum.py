#You will receive a single number. You have to write a function that returns the sum of
# all even and all odd digits from that number as a single string like in the examples below.
#  1000435 -->	 Odd sum = 9, Even sum = 4
def return_sum_of_even_and_odd(num):
    even_sum = 0
    odd_sum = 0
    for n in num:
        if int(n) % 2 ==0:
            even_sum += int(n)
        else:
            odd_sum += int(n)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

number = input()
return_sum_of_even_and_odd(number)
