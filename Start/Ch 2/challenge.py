# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: use inheritance and abstract classes

# Challenge: create a class structure to represent stocks and bonds
# Requirements:
# -- Both stocks and bonds have a price
# -- Stocks have a company name and ticker
# -- Bonds have a description, duration, and yield
# -- You should not be able to instantiate the base class
# -- Subclasses are required to override get_description()
# -- get_description returns formats for stocks and bonds
# For stocks: "Ticker: Company -- $Price"
# For bonds: "description: duration'yr' : $price : yieldamt%"

from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, price: float):
        self.price = price
    @abstractmethod
    def get_description(self) -> str:
        pass

class Stock(Asset):
    def __init__(self, ticker: str, price: float, company: str):
        super().__init__(price)
        self.ticker = ticker
        self.company = company
    def get_description(self) -> str:
        return f"{self.ticker}: {self.company} -- ${self.price:.1f}"

class Bond(Asset):
    def __init__(self, price: float, description: str, duration: int, interest: float):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.interest = interest
    def get_description(self) -> str:
        return f"{self.description}: {self.duration} : ${self.price:.1f} : {self.interest:.2f}%"

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
try:
   ast = Asset(100.0) # type: ignore
except:
   print("Can't instantiate Asset!")

msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

us30yr = Bond(95.31, "30 Year US Treasury", 30, 4.38)
us10yr = Bond(96.70, "10 Year US Treasury", 10, 4.28)
us5yr = Bond(98.65, "5 Year US Treasury", 5, 4.43)
us2yr = Bond(99.57, "2 Year US Treasury", 2, 4.98)

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())

print(us30yr.get_description())
print(us10yr.get_description())
print(us5yr.get_description())
print(us2yr.get_description())
