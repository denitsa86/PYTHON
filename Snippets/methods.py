# When to Use @staticmethod
# Use it when:
# The method doesn’t need to access or modify instance or class variables.
# You want to group related functionality inside the class for clarity.
# 1. Instance Method (default method type)
# Accesses: self → the instance of the class
# Use case: When the method needs to access or modify instance attributes
#
# class Book:
#     def display_info(self):
#         print(f"{self.name} by {self.author}")
# You call it like:
# python
# book = Book(...)
# book.display_info()
# 2. Class Method (@classmethod)
# Accesses: cls → the class itself
# Use case: When the method needs to access or modify class-level data, or create instances in alternative ways
# class Book:
#     @classmethod
#     def from_dict(cls, data):
#         return cls(**data)
# You call it like:
#book = Book.from_dict({...})
# 3. Static Method (@staticmethod)
# Accesses: Nothing — no self, no cls
# Use case: Utility functions that relate to the class but don’t need access to instance or class data
#
# class Book:
#     @staticmethod
#     def is_valid_price(price):
#         return float(price) > 0
# You call it like:
# Book.is_valid_price("19.99")