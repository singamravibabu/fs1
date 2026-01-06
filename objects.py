class Product:
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent
    def discountAmount(self):
        return self.price * self.discountPercent / 100
    def discountPrice(self):
        return self.price - self.discountAmount()
    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nDiscount percent: {self.discountPercent}\nDiscount amount: {self.discountAmount()}\nDiscount price: {self.discountPrice()}"