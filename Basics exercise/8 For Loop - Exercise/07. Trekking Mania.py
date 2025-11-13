# •	Група до 5 човека – изкачват Мусала
# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест
#програма, която изчислява процента на катерачите изкачващи всеки връх.
# броя на групите от катерачи – цяло число [1...1000]
# За всяка група на отделен ред – броя на хората в групата – цяло число  [1...1000]
count_groups = int(input())
musala_group = 0
montblan_group = 0
cilimandjaro_group = 0
k_two_group = 0
everest_group = 0

for groups in range(count_groups):
    members = int(input())
    if members <= 5:
        musala_group += members
    elif members <= 12:
        montblan_group += members
    elif members <= 25:
        cilimandjaro_group += members
    elif members <= 40:
        k_two_group += members
    elif members > 40:
        everest_group += members
total_people = musala_group + montblan_group + cilimandjaro_group + k_two_group + everest_group
# 6 / 326 * 100 = 1.84%
musala_percatage = musala_group / total_people * 100
montblan_percatage = montblan_group / total_people * 100
cilimandjaro_percatage = cilimandjaro_group / total_people * 100
k_two_percatage = k_two_group / total_people * 100
everest_percatage = everest_group / total_people * 100
print(f"{musala_percatage:.2f}%")
print(f"{montblan_percatage:.2f}%")
print(f"{cilimandjaro_percatage:.2f}%")
print(f"{k_two_percatage:.2f}%")
print(f"{everest_percatage:.2f}%")
