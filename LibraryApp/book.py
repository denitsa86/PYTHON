class Book:
    def __init__(self, name, author, theme, price, location, resellable):
        self.name = name
        self.author = author
        self.theme = theme
        self.price = float(price)
        self.location = location
        self.resellable = resellable

    def to_list(self):
        return [self.name, self.author, self.theme, self.price, self.location, self.resellable]

    @staticmethod
    def from_list(data):
        name, author, theme, price, location, resellable = data
        return Book(name, author, theme, float(price), location, resellable == "True")

    def __str__(self):
        return f"{self.name} by {self.author} | {self.theme} | {self.price:.2f} | {self.location} | Resellable: {self.resellable}"
