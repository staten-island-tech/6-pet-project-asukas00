
class Pet:
    def __init__(self, name, happiness, hygiene, thirst, hunger, energy):
        self.name = name
        self.happiness = happiness
        self.hygiene = hygiene
        self.thirst = thirst
        self.hunger = hunger
        self.energy = 5
    def play(self):
        if self.energy > 0:
            self.happiness += 10
            self.energy -= 1
            print(f"{self.name} is playing catch!")
            print(f"Happiness increased to {self.happiness}, energy now {self.energy}")
            self.hunger -=10
            self.hygiene -= 10
            self.thirst -= 10
            print(f"Happiness:{self.happiness} hygiene: {self.hygiene} thirst: {self.thirst} full: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play.")

    def bath(self, hygiene):
        if self.hygiene > 80:
            self.energy -= 1
            print(f"{self.name} is now clean")
            print(f"{Petname} has {self.energy} energy left")
            self.hunger -= 10
            print(f"Happiness:{self.happiness} hygiene: {self.hygiene} thirst: {self.thirst} full: {self.hunger}")
        else: 
            print(f"{self.name} took a bath")
            self.hygiene += 10
            print(f"{self.name}'s hygiene increased to {hygiene}")
            self.energy -= 1
            print(f"{Petname} has {self.energy} energy left")
            self.hunger -= 10
            print(f"Happiness:{self.happiness} hygiene: {self.hygiene} thirst: {self.thirst} full: {self.hunger}")
    def drink(self):
        if self.thirst > 80:
            print(f"{self.name} is now hydrated")
            energy -= 1
            print(f"{Petname} has {self.energy} energy left")
            print(f"Happiness:{self.happiness} hygiene: {self.hygiene} thirst: {self.thirst} full: {self.hunger}")
        else:
            print(f"{self.name} drank some water")
            self.thirst += 10
            print(f"{self.name}'s hydration increased to {self.thirst}")
            self.energy -= 1
            print(f"{Petname} has {self.energy} energy left")
            print(f"Happiness:{self.happiness} hygiene: {self.hygiene} thirst: {self.thirst} full: {self.hunger}")
            if self.energy == 0:
                print(f"{self.name} is now tired")
                print(f"Happiness:{self.happiness} hygiene: {self.hygiene} thirst: {self.thirst} full: {self.hunger}")
    def eat(self):
        if self.hunger > 80:
            print(f"{self.name} is now realy full")
            self.energy += 1
            print(f"{Petname} has {self.energy} energy left")
            print(f"Happiness:{self.happiness} hygiene: {self.hygiene} thirst: {self.thirst} full: {self.hunger}")
        else: 
            print(f"{self.name} ate some food")
            self.hunger += 20
            print(f"{self.name}'s hunger increased to {self.hunger}")
            self.energy += 1
            print(f"{Petname} has {self.energy} energy left")
            print(f"Happiness:{self.happiness} hygiene: {self.hygiene} thirst: {self.thirst} full: {self.hunger}")
    def death(self):
        if self.thirst <= 0 or self.hunger <= 0:
            print(f"{self.name} died. Please take better care of yout pet next time!!!")

Yourname = input("what is your name?:")
Petname = input("what is your pet's name?:")

Pname = Pet(f"{Petname}", 40, 50, 50, 50, 5)

story = print(f"You come home with {Petname} after buying them from the store ")
game = True
while game == True:
    action = input("What do you want to do with your pet? play/bath/drink/eat/quit: ")
    self = Pname
    if action == "play":
        self.play()
    elif self.thirst <= 0 or self.hunger <= 0:
        game = False
        self.death()
    elif action == "bath":
        self.bath(self.hygiene)
    elif action == "drink":
        self.drink()
    elif action == "eat":
        self.eat()
    elif action == "quit":
        print(f"Goodbye! {Petname} wags his tail at you!")
        break
    if self.thirst <= 0 or self.hunger <= 0:
        self.death()
        break
    if action not in ["play", "bath" , "drink" , "eat"]:
        print("Invalid action. Please choose play/bath/drink/eat/quit.")
        