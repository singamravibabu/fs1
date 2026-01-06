import random

class Die:
    def __init__(self):
        self.__value = 1
    # getter method
    def getValue(self):
        return self.__value
    # setter method
    def setValue(self, value):
        if value < 1 or value > 6:
            raise ValueError("Die value must be between 1 and 6")
        else:
            self.__value = value
    def roll(self):
        self.__value = random.randint(1, 6)
        
class Dice:
    def __init__(self):
        self.__list = []
    def rollAll(self):
        for die in self.__list:
            die.roll()
    def addDie(self, die):
        self.__list.append(die)