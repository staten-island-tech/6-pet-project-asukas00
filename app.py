
class Pet:
    def __init__(self, name, happiness, hygiene, thirst, hunger, energy):
        self.name = name
        self.happiness = happiness
        self.hygiene = hygiene
        self.thirst = thirst
        self.hunger = hunger
        self.energy = 5
        self.death = False
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

    def bath(self, hygiene):
        if self.hygiene > 80:
            self.energy -= 1
            print(f"{self.name} is now clean")
            print(f"{Petname} has {self.energy} energy left")
            self.hunger -= 10
        else: 
            print(f"{self.name} took a bath")
            self.hygiene += 10
            print(f"{self.name}'s hygiene increased to {hygiene}")
            self.energy -= 1
            print(f"{Petname} has {self.energy} energy left")
    def drink(self):
        if self.thirst > 80:
            print(f"{self.name} is now hydrated")
            energy -= 1
            print(f"{Petname} has {self.energy} energy left")
        else:
            print(f"{self.name} drank some water")
            self.thirst += 10
            print(f"{self.name}'s hydration increased to {self.thirst}")
            self.energy -= 1
            print(f"{Petname} has {self.energy} energy left")
            if self.energy == 0:
                print(f"{self.name} is now tired")
    def eat(self):
        if self.hunger > 80:
            print(f"{self.name} is now realy full")
            self.energy += 1
            print(f"{Petname} has {self.energy} energy left")
        else: 
            print(f"{self.name} ate some food")
            self.hunger += 20
            print(f"{self.name}'s hunger increased to {self.hunger}")
            self.energy += 1
            print(f"{Petname} has {self.energy} energy left")
    def death(self):
        if self.hygiene == 0 or self.thirst == 0 or self.hunger == 0:
            self.death = True
            print(f"{Pname} died. Please take better care of yout pet next time!!!")

Yourname = input("what is your name?:")
Petname = input("what is your pet's name?:")

Pname = Pet(f"{Petname}", 50, 50, 50, 50, 5)

story = input(f"You come home with {Petname} after buying them from the store ")

while True:
    action = input("What do you want to do with your pet? play/bath/drink/eat/quit: ")
    self = Pname
    if action == "play":
        self.play()
    if action != "play":
        self.happiness -= 10
    elif action == "bath":
        self.bath(self.hygiene)
    elif action == "drink":
        self.drink()
    elif action == "eat":
        self.eat()
    elif action == "quit":
        print(f"Goodbye! {Petname} wags his tail at you!")
        break
    else:
        print("Invalid action. Please choose play/bath/drink/eat/quit.")
        if self.thirst <= 0 or self.hunger <= 0:
            self.death()