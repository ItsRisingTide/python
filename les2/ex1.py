from decimal import *

# "base" : "RUB" // "date": "10.05.2020"
rates =  {
    "EUR" : "0.0124993907",
    "USD" : "0.0135368371",
    "GBP" : "0.0109817703",
    "CAD" : "0.0190941780" ,
    "INR" : "1.0291242153",
    "RUB" : "1",
    }
# Euro Member Countries, Euro
# United States, Dollar
# United Kingdom, Pound
# Canada, Canadian Dollar
# India, Rupee

_formats = {
    "RUB" : "₽",
    "EUR" : "€",
    "USD" : "$",
    "GBP" : "£",
    "CAD" : "$" ,
    "INR" : "₹",
}

class Money:
    """Class representing a monetary amount"""

    def __init__(self, amount, currency):
        if currency in rates:
            self._amount = Decimal(amount)
            self._currency = currency
        else:
            raise TypeError("such currency isn't used")

    @staticmethod
    def convert(amount, from_currency, to_currency):
        if from_currency != "RUB":
            amount = amount / Decimal(rates[from_currency])
        if to_currency == "RUB":
            return amount
        else:
            return amount * Decimal(rates[to_currency])

    def __add__(self, other):
        if (isinstance(other, Money)):
            return Money(self._amount +
                    + self.convert(other._amount, other._currency, self._currency), self._currency)
        elif (isinstance(other, int)):
            return Money(self._amount + Decimal(other), self._currency)
        else:
            NotImplemented

    def __radd__ (self,other):
        return self.__add__(other)

    def __repr__(self):
        return f'Money({(self._amount)},{self._currency})'

    def __str__(self):
        return f"{_formats[self._currency]}{(self._amount).quantize(Decimal('.0001'))}"



m1 = Money(100, "USD")
m2 = Money(100, "EUR")
m3 = Money(100, "RUB")
print(f"{m1} + {m2} --> {m1 + m2}")
print(f"{m3} + {m1} --> {m3 + m1}")
print(f"{m2} + {m3} --> {m2 + m3}")
print(f"{m1} + {3} --> {m1 + 3}")
print(f"{3} + {m1} --> {3 + m1}")
