#Да се напише програма, която чете число n, въведено от потребителя, и печата четните
# степени на 2 ≤ 2n: 20, 22, 24, 26, …, 2n.
import math
number = int(input())
for i in range(0, 2 * number + 1, 2):
    print(int(math.pow(2, i)))