# програма, която изчислява броя на парчетата, които гостите са взели преди тя да свърши. Ще получите
# размерите на тортата (широчина и дължина – цели числа и след това на всеки ред, до получаване на
# командата "STOP" или докато не свърши тортата, броят на парчетата, които гостите вземат от нея.
# Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# •	"{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# •	"No more cake left! You need {брой недостигащи парчета} pieces more."
import math
width_cake = int(input())
length_cake = int(input())
total_pieces_available = width_cake * length_cake
slices_taken = input()
while slices_taken.isdigit():
    total_pieces_available -= int(slices_taken)
    if total_pieces_available <= 0:
        break
    else:
        slices_taken = input()
if total_pieces_available <= 0:
    print(f"No more cake left! You need {int(math.fabs(total_pieces_available))} pieces more.")
elif total_pieces_available > 0:
    print(f"{total_pieces_available} pieces are left.")

