from abc import ABC,abstractmethod

# 1. ABSTRACTION: A blueprint for all store items
class Item(ABC):
    @abstractmethod
    def get_details(self):
        pass

# 2. ENCAPSULATION: Base class with protected price data
class Product(Item):
    def __init__(self,name,price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def get_details(self):
        return f'{self.name} - ${self.__price:.2f}'

# A separate parent class for items that can have discounts
class Discountable:
    def __init__(self, discount_percent):
        self.discount_percent = discount_percent

    def get_discount_info(self):
        return f'{self.discount_percent}%OFF'
    
# 3. MULTIPLE INHERITANCE: Inherits from BOTH Product and Discountable
class ClearanceBook(Product,Discountable):
    def __init__(self,name,price,author,discount_percent):
        Product.__init__(self,name,price)
        Discountable.__init__(self,discount_percent)
        self.author = author

    # 4. POLYMORPHISM: Overriding get_details to use features from both parents
    def get_details(self):
        basic_info = f"Book: '{self.name}' by {self.author}"
        price_info = f"${self.get_price():.2f}"
        deal_info = self.get_discount_info()

        return f'{basic_info} - {price_info} [{deal_info}]'

# Creating a regular product (Single Inheritance from Item)
regular_item = Product("Coffee Mug", 12.00)

# Creating a clearance book (Multiple Inheritance)
sale_book = ClearanceBook("Python Basics", 40.00, "John Doe", 20)

# Polymorphism in action
print(regular_item.get_details())
print(sale_book.get_details())


    
