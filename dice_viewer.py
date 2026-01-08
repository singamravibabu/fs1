from dice import Die, Dice

num = int(input("Enter the number of dice you want to roll: "))

dice = Dice()

for i in range(num):
    die = Die()
    dice.addDie(die)

dice.rollAll()
for die in dice.getList():
    print(die.getValue(), end=" ")