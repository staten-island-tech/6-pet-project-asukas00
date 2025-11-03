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
    def __init__(self, name, happiness, hygiene, thirst, hunger, energy):
        self.name = name
        self.happiness = happiness
        self.hygiene = hygiene
        self.thirst = thirst
        self.hunger = hunger
        self.energy = energy

    def play(self):
        if self.happiness > 80:
            print(f"{self.name} is already very happy!")
        elif self.energy > 0:
            self.happiness += 10
            self.energy -= 1
            print(f"{self.name} is playing catch!")
            print(f"Happiness increased to {self.happiness}, energy now {self.energy}")
        else:
            print(f"{self.name} is too tired to play.")

    def bath(self):
        if self.hygiene >= 80:
            print(f"{self.name} is already clean.")
        else:
            self.hygiene += 10
            self.energy -= 1
            print(f"{self.name} took a bath! Hygiene: {self.hygiene}, Energy: {self.energy}")

    def drink(self):
        if self.thirst >= 80:
            print(f"{self.name} is already hydrated.")
        else:
            self.thirst += 10
            self.energy -= 1
            print(f"{self.name} drank some water! Thirst: {self.thirst}, Energy: {self.energy}")

    def eat(self):
        if self.hunger >= 80:
            print(f"{self.name} is already full.")
        else:
            self.hunger += 20
            self.energy += 1
            print(f"{self.name} ate some food! Hunger: {self.hunger}, Energy: {self.energy}")

    def check_death(self):
        if self.hygiene <= 0 or self.thirst <= 0 or self.hunger <= 0:
            print(f"{self.name} died 💀 Please take better care of your pet next time!")
            return True
        return False


# --- Game Setup ---
your_name = input("What is your name?: ")
pet_name = input("What is your pet's name?: ")

pet = Pet(pet_name, 50, 50, 50, 50, 5)
print(f"You come home with {pet.name} after buying them from the store!")

# --- Game Loop ---
while True:
    action = input("\nWhat do you want to do with your pet? play/bath/drink/eat/quit: ").lower()

    if action in ["play", "p"]:
        pet.play()
    elif action in ["bath", "b"]:
        pet.bath()
    elif action in ["drink", "d"]:
        pet.drink()
    elif action in ["eat", "e"]:
        pet.eat()
    elif action in ["quit", "q"]:
        print(f"Goodbye! {pet.name} waves at you!")
        break
    else:
        print("Invalid action. Please choose play/bath/drink/eat/quit.")

    # Check if the pet dies
    if pet.check_death():
        break
