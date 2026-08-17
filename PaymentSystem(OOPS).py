from abc import ABC, abstractmethod

# ABSTRACTION
class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass


# ENCAPSULATION + DATA HIDING
class UPI(Payment):

    def __init__(self, balance):
        self.__balance = balance       # Data hiding

    def pay(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"UPI Payment of ₹{amount} successful")
        else:
            print("Insufficient balance")


class Card(Payment):

    def __init__(self, balance):
        self.__balance = balance       # Data hiding

    def pay(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Card Payment of ₹{amount} successful")
        else:
            print("Insufficient balance")


# DYNAMIC BINDING (Encapsulation)
upi = UPI(5000)
upi.pay(1000)

card = Card(5000)
card.pay(2000)
