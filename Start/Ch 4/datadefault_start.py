# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass
from dataclasses import field
import random

def price_func():  
    # this function can be used to set a default value
    return float(random.randrange(20, 40))  # random price between 20 and 40

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)


b1 = Book()
print(b1)
b2 = Book("War and Peace", "Leo Tolstoy", 1225)
b3 = Book("The Catcher in the Rye", "JD Salinger")
print(b2)
print(b3)