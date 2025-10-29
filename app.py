class Calculator():
    def add(x,y):
        print(x+y)
        return x + y
    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)
    def subtract(numbers):
        return numbers
""" Calculator.add(5,10) """
""" Calculator.add_many([4,7,9]) """

class Hero:
    def __init__(self, name, money, inventory, strength, intelligence, endurnance):
        self.name = name
        self.money = money
        self.inventory = inventory 
        self.strength = strength
        self.intelligence = intelligence
        self.endurance = endurnance
    def buy(self,item):
        self.inventory.append(item)
        print(self.inventory)
Juice = Hero("Juice", 50, [], 5,5,5)
Juice.buy({"title": "Dull_Blade","atk": 10})
print(Juice.__dict__)