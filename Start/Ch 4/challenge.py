# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: implement a dataclass

# Challenge: convert your classes to dataclasses
# The subclasses are required to override the magic method
# that makes them sortable

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from functools import total_ordering

@total_ordering
@dataclass
class Asset(ABC):
    value: float

    @abstractmethod
    def __lt__(self, other): pass

@dataclass
class Stock(Asset):
    symbol: str
    company: str

    def __lt__(self, other):
        if not isinstance(other, Stock):
            return NotImplemented
        return self.symbol < other.symbol

    def __str__(self):
        return f"{self.symbol}: {self.value} ({self.company})"

@dataclass
class Bond(Asset):
    name: str
    maturity: int
    rate: float

    def __lt__(self, other):
        if not isinstance(other, Bond):
            return NotImplemented
        return self.maturity < other.maturity

    def __str__(self):
        return f"{self.name}: {self.value}, {self.maturity}Y @ {self.rate}%"

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
stocks = [
    Stock(342.0, "MSFT", "Microsoft Corp"),
    Stock(135.0, "GOOG", "Google Inc"),
    Stock(275.0, "META", "Meta Platforms Inc"),
    Stock(120.0, "AMZN", "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]

try:
   ast = Asset(100.0) # type: ignore
except:
   print("Can't instantiate Asset!")

stocks.sort()
bonds.sort()

for stock in stocks:
   print(stock)
print("-----------")
for bond in bonds:
   print(bond)
