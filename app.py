""" class Calculator():
    def add(x,y):
        print(x+y)
        return x + y
    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)
    def subtract(numbers):
        return numbers """
""" Calculator.add(5,10) """
""" Calculator.add_many([4,7,9]) """

""" class Hero:
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
print(Juice.__dict__) """

class Pet:
    def __init__(self, name, happiness, hygiene, thrist, hunger):
        self.name = name
        self.happiness = happiness
        self.hygiene = hygiene
        self.thirst = thrist
        self.hunger = hunger
    def play(self, happy):
        if happy > 80:
            print(f"{self.name} is now happy")
        else:
            self.happiness += happy
            print(f"{self.name} is playing catch")
            print(f"{self.name}'s increased to {self.happiness}")
    def bath(self, hygiene):
        if hygiene > 80:
            print(f"{self.name} is now clean")
        else: 
            print(f"{self.name} took a bath")
            hygiene += 10
            print(f"{self.name}'s hygiene increased to {hygiene}")
    def drink(self, thirst):
        if thirst > 80:
            print(f"{self.name} is now hydrated")
        else: 
            print(f"{self.name} drank some water")
            thirst += 10
            print(f"{self.name}'s hydration increased to {thirst}")
    def eat(self, hunger):
        if hunger > 80:
            print(f"{self.name} is now realy full")
        else: 
            print(f"{self.name} ate some food")
            hunger += 20
            print(f"{self.name}'s hunger increased to {hunger}")
Yourname = input("what is your name?:")
Petname = input("what is your pet's name?:")
Pname = Pet("{Petname}", 50, 50, 50, 50)

while True:
    x = input("what do u want to do with your pet?: play, bath, drink or eat.(p/b/d/e)")
    if x == ('play') or x == ('p'):
        Pname.play(10)
    
