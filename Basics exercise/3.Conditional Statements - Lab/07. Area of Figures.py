import math
# въвежда вида и размерите на геометрична фигура и пресмята лицето й.
# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle)
# и триъгълник (triangle). На първия ред на входа се чете вида на фигурата
# (текст със следните възможности: square, rectangle, circle или triangle).
# квадрат (square): на сл ред се чете едно дробно число дължина на страната му
# правоъгълник (rectangle):две дробни числа - дължините на страните му
# кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# триъгълник (triangle): две дробни числа - дълж на страната му и дълж на височината
# към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.
#square=a*a; rectangle=a*b; triangle = a*ha/2; circle=π r²
figure = input()
if figure == "square":
    square_side = float(input())
    print(f"{square_side * square_side:.3f}")
elif figure == "rectangle":
    rectangle_side_one = float(input())
    rectangle_side_two = float(input())
    print(f"{rectangle_side_one * rectangle_side_two:.3f}")
elif figure == "circle":
    radius = float(input())
    print(f"{math.pi * radius ** 2:.3f}")
else:
    triangle_side = float(input())
    triangle_height = float(input())
    print(f"{triangle_side * triangle_height / 2:.3f}")
