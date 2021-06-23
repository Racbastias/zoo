class Zoo: #working
    def __init__(self, name):
        self.name = name
        self.animals = []
    
    def add_animal(self, animal): #working
        self.animals.append(animal)
        return self
    
    def zoo_information(self):#notworkingwell
        for animal in self.animals:
            return f"Type: {animal.name}\n Name:{animal.nickname}\n Age: {animal.age}\n"

class Animal: #working
    
    def __init__(self, name, nickname, size, age, health, happyness):
        self.name = name
        self.nickname = nickname
        self.size = size
        self.age = age
        self.health = health
        self.happyness = happyness
    
    def display_info(self): #working
        return (f"This {self.name} called {self.nickname} have an {self.health}% of healthy, and is {self.happyness}% happy at the moment")
    
    def feed(self, food): #working
        self.health += food.healthQ
        if self.health >= 100:
            self.health = 100
            return (f"You gave an {food.name} to {self.nickname}. Congrats! {self.nickname} have 100% of health!")
        elif self.health <= 0:
            self.health = 0
            return (f"You gave an {food.name} to {self.nickname}. What are you doing!!?? {self.nickname} is critical!!!")
        elif self.health <50:
            return (f"You gave an {food.name} to {self.nickname}. {self.nickname} the {self.name} have {self.health}% of health, wich is not so good")
        elif self.health >50:
            return (f"You gave an {food.name} to {self.nickname}. {self.nickname} have {self.health}% of health, wich is quiet good")
        self.happyness += food.happyQ
        if self.happyness >= 100:
            self.happyness = 100
            return (f"You gave an {food.name} to {self.nickname}. Congrats! {self.nickname} have 100% of hapyness!")
        elif self.happyness <= 0:
            self.happyness = 0
            return (f"You gave an {food.name} to {self.nickname}. What are you doing!!?? {self.nickname} have depression and start trying drugs!!")
        elif self.happyness <50:
                return (f"You gave an {food.name} to {self.nickname}. {self.nickname} have {self.happyness}% of health, wich is not so good")
        elif self.happyness >50:
            return (f"You gave an {food.name} to {self.nickname}. {self.nickname} have {self.happyness}% of health, wich is quiet good")
    
    def exercise(self):
        raise NotImplementedError

class Food: #working
    def __init__(self, name, healthQ, happyQ):
        self.name = name
        self.healthQ = healthQ
        self.happyQ = happyQ

class Marines(Animal): #not tested
    def __init__(self, name, nickname, size, age, health, happyness):
        super().__init__(name, nickname, size, age, health, happyness)
        self.swimming = True
    
    def exercise(self, distance):
        if self.swimming == True:
            self.distance = distance
            self.health -= distance
            if self.health <= 0:
                self.health = 0
                return (f"{self.nickname} has swam {self.distance} kms, and now is totally exhausted. His health is {self.health}%")
            elif self.health <50:
                return (f"{self.nickname} has swam {self.distance} kms, and now is almost exhausted. His health is {self.health}% ")
            elif self.health >50:
                return (f"{self.nickname} has swam {self.distance} kms, but is so strong. His health is {self.health}%")
        return self

class Earthlys(Animal):
    def __init__(self, name, nickname, size, age, health, happyness):
        super().__init__(name, nickname, size, age, health, happyness)
        self.walking = True
    
    def exercise(self, distance):
        if self.walking == True:
            self.distance = distance
            self.health -= distance
            if self.health <= 0:
                self.health = 0
                return (f"{self.nickname} has walked {self.distance} kms, and now is totally exhausted. His health is {self.health}%")
            elif self.health <50:
                return (f"{self.nickname} has walked {self.distance} kms, and now is almost exhausted. His health is {self.health}% ")
            elif self.health >50:
                return (f"{self.nickname} has walked {self.distance} kms, but is so strong. His health is {self.health}%")
        else:
            return (f"I'm afraid this animal can't walk")

class Aerials(Animal): #not tested
    def __init__(self, name, nickname, size, age, health, happyness):
        super().__init__(name, nickname, size, age, health, happyness)
        self.flying = True
    
    def exercise(self, distance):
        if self.flying == True:
            self.distance = distance
            self.health -= distance
            if self.health <= 0:
                self.health = 0
                return (f"{self.nickname} has flew {self.distance} kms, and now is totally exhausted. His health is {self.health}%")
            elif self.health <50:
                return (f"{self.nickname} has flew {self.distance} kms, and now is almost exhausted. His health is {self.health}% ")
            elif self.health >50:
                return (f"{self.nickname} has flew {self.distance} kms, but is so strong. His health is {self.health}%")
        else:
            return (f"I'm afraid this animal can't fly")
