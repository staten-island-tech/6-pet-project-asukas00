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
    def __init__(self, name, happiness, hygiene, thrist, hunger, energy):
        self.name = name
        self.happiness = happiness
        self.hygiene = hygiene
        self.thirst = thrist
        self.hunger = hunger
        self.energy = energy
        energy = 5
    def play(self, happy, energy):
        if ('play') == x or ('p') == x:
            if happy > 80:
                    print(f"{self.name} is now happy")
                    energy -= 1
            elif energy > 0 and happy < 80:
                self.happiness += happy
                energy -= 1
                print(f"{self.name} is playing catch")
                print(f"{self.name}'s increased to {self.happiness}")
                print(f"{Pname} now has only {energy} more energy")
            else:
                print(f"{Pname} is too tired to play. ")
    def bath(self, hygiene):
        if ('bath') == x or ('b') == x:
            if hygiene > 80:
                energy -= 1
                print(f"{self.name} is now clean")
            else: 
                print(f"{self.name} took a bath")
                hygiene += 10
                print(f"{self.name}'s hygiene increased to {hygiene}")
                energy -= 1
    def drink(self, thirst):
        if ('drink') == x or ('d') == x:
            if thirst > 80:
                print(f"{self.name} is now hydrated")
                energy -= 1
            else: 
                print(f"{self.name} drank some water")
                thirst += 10
                print(f"{self.name}'s hydration increased to {thirst}")
                energy -= 1
    def eat(self, hunger):
        if hunger > 80:
            print(f"{self.name} is now realy full")
            energy += 1
        else: 
            print(f"{self.name} ate some food")
            hunger += 20
            print(f"{self.name}'s hunger increased to {hunger}")
            energy += 1

Yourname = input("what is your name?:")
Petname = input("what is your pet's name?:")
Pname = Pet(f"{Petname}", 50, 50, 50, 50, 5)
x = input("What do you want to do with your pet?(play,bath,eat,drink)")
