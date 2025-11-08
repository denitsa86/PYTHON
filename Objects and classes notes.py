class Person:  # class is keyword, Person - name of the class
    def __init__(self, name, age, kg):   #attributes
        self.name = name
        self.age = age
        self.kg = kg

person = Person("Test", 12, 30) # automatically calls the magic init method- className()
p2 = Person("Deni", 15, 44)
a = 5