names = ["kari", "lila", "deya"]

def name_generator(names):
    for name in names:
        yield name

my_generator = name_generator(names)
try:
    print(next(my_generator))
    print(next(my_generator))
    print(next(my_generator))
    print(next(my_generator))
except StopIteration:
    print("No more students")
