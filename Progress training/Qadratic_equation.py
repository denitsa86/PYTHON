import math
import cmath
# ax**2 + bx + c=0
# x1,x2=b+-sqrt(b**2-4ac)/2a
#Входни данни
a=2
b=1
c=-3
#Намираме дискриминантата
d=b**2-4*a*c
#Ако дискриминантата > 0, има 2 реални корена
if d>0:
 x_one = (-b+math.sqrt(d))/(2*a)
 x_two = (-b-math.sqrt(d))/(2*a)
 print("Real roots:")
 print(x_one)
 print(x_two)
#Ако дискриминантата е 0, има 1 реален корен
elif d==0:
 x_zero = -b/(2*a)
 print("One real root:")
 print(x_zero)
#Ако нискриминантата < 0, няма реални корени
else:
 d_complex = cmath.sqrt(b**2 - 4*a*c)
 x_com1 = (-b + d_complex) / (2*a)
 x_com2 = (-b - d_complex) / (2*a)
 print("Complex roots:")
 print(x_com1)
 print(x_com2)



