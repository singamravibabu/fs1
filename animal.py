class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def speaks(self):
        return 'Animal makes a sound'
class Dog(Animal):
    def __init_(self, name, age, color, breed, type):
        Animal.__init__(self, name, age, color)
        self.breed = breed
        self.type = type
    def speaks(self):
        return 'Dog barks'