
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
        else: 
            print(f"{self.name} took a bath")
            self.hygiene += 10
            print(f"{self.name}'s hygiene increased to {hygiene}")
            self.energy -= 1
    def drink(self):
        if self.thirst > 80:
            print(f"{self.name} is now hydrated")
            energy -= 1
        else:
            print(f"{self.name} drank some water")
            self.thirst += 10
            print(f"{self.name}'s hydration increased to {self.thirst}")
            self.energy -= 1
            if self.energy == 0:
                print(f"{self.name} is now tired")
    def eat(self):
        if self.hunger > 80:
            print(f"{self.name} is now realy full")
            self.energy += 1
        else: 
            print(f"{self.name} ate some food")
            self.hunger += 20
            print(f"{self.name}'s hunger increased to {self.hunger}")
            energy += 1
    def death(self,hygiene, thrist, hunger):
        if hygiene == 0 or thrist == 0 or hunger == 0:
            print(f"{Pname} died. Please take better care of yout pet next time!!!")
            self.death = True

Yourname = input("what is your name?:")
Petname = input("what is your pet's name?:")

Pname = Pet(f"{Petname}", 50, 50, 50, 50, 5)

story = input(f"You come home with {Petname} after buying them from the store ")

action = input("What do you want to do with your pet? play/bath/drink/eat/quit: ")
while self.energy > 0:
    self = Petname
    if action in "play":
        self.play(self)
    elif action in "bath":
        self.bath(self)
    elif action in "drink":
        self.drink(self)
    elif action in "eat":
        self.eat(self)
    elif action in "quit":
        print(f"Goodbye! {Petname} wags his tail at you!")
        break
    else:
        print("Invalid action. Please choose play/bath/drink/eat/quit.")