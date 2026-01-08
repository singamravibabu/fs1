class Product:
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.__price = price
        self.discountPercent = discountPercent
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        else:
            self.__price = price
    def discountAmount(self):
        return self.__price * self.discountPercent / 100
    def discountPrice(self):
        return self.__price - self.discountAmount()
    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.__price}\nDiscount percent: {self.discountPercent}\nDiscount amount: {self.discountAmount()}\nDiscount price: {self.discountPrice()}"