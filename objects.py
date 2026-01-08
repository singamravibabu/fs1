class Product:
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
    def getDescription(self):
        return self.name
class Book(Product):
    def __init__(self, name, price, discountPercent, author):
        Product.__init__(self, name, price, discountPercent)
        self.author = author
    def getDescription(self):
        return self.name + " by " + self.author
class Movie(Product):
    def __init__(self, name, price, discountPercent, year):
        Product.__init__(self, name, price, discountPercent)
        self.year = year
    def getDescription(self):
        return self.name + " (" + str(self.year) + ")"