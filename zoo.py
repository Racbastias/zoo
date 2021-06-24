class Zoo: #working
    def __init__(self, name):
        self.name = name
        self.animals = []
    
    def add_animal(self, animal): #working
        self.animals.append(animal)
        return self
    
    def zoo_information(self):
        print(f"\n The {self.name}`s animals are: \n")
        for i in range (len(self.animals)):
            print(i, '= ', self.animals[i])
        return (f"As you can count, there are {len(self.animals)} animals in the Zoo today. ¡Have fun!")
    
    def add_water(self, name, nickname, size, age):
        newwater = Water(name, nickname, size, age)
        self.animals.append(newwater)
    
    def add_land(self, name, nickname, size, age):
        newland = Land(name, nickname, size, age)
        self.animals.append(newland)
        
    def add_sky(self, name, nickname, size, age):
        newsky = Sky(name, nickname, size, age)
        self.animals.append(newsky)
        

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
    
    def __repr__(self):
        return f"{self.nickname} the {self.name} has {self.health}% of health and {self.happyness}% of happynes"
    
    def exercise(self):
        raise NotImplementedError
    
    def feed(self, food): #working
        self.health += food.healthQ
        if self.health >= 100:
            self.health = 100
            print(f"You gave an {food.name} to {self.nickname}. Congrats! {self.nickname} have 100% of health!")
        elif self.health <= 0:
            self.health = 0
            print(f"You gave an {food.name} to {self.nickname}. What are you doing!!?? {self.nickname} is critical!!!")
        elif self.health <50:
            print(f"You gave an {food.name} to {self.nickname}. {self.nickname} the {self.name} have {self.health}% of health, wich is not so good")
        elif self.health >50:
            print(f"You gave an {food.name} to {self.nickname}. {self.nickname} have {self.health}% of health, wich is quiet good")
        self.happyness += food.happyQ
        if self.happyness >= 100:
            self.happyness = 100
            print(f"Also, {self.nickname} have 100% of hapyness!")
        elif self.happyness <= 0:
            self.happyness = 0
            print(f"Also, {self.nickname} have {self.happyness}% of happyness, so fall in depression and start trying drugs!!")
        elif self.happyness <50:
            print(f"Also, {self.nickname} have {self.happyness}% of health, wich is not so good, take care!")
        elif self.happyness >50:
            print(f"Also, {self.nickname} have {self.happyness}% of health, wich is quiet good")
        return('Eat is good, but eat too much could be a problem')

class Food: #working
    def __init__(self, name, ):
        self.name = name
        self.foods = []
        
    def add_food(self, food):
        self.foods.append(food)
        return self
    
    def __repr__(self):
        return f"{self.name}"

class Foods(Food):
    def __init__(self, name, healthQ, happyQ):
        super().__init__(name)
        self.healthQ = healthQ
        self.happyQ = happyQ
        
class Water(Animal): #working
    def __init__(self, name, nickname, size, age, health=50, happyness=50):
        super().__init__(name, nickname, size, age, health, happyness)
        self.swimming = True
    
    def exercise(self, distance):
        if self.swimming == True:
            self.distance = distance
            self.health -= distance
            self.happyness += distance
            if self.health <= 0:
                self.health = 0
                return (f"{self.nickname} has swam {self.distance} kms, and now is totally exhausted. His health is {self.health}%")
            elif self.health <50:
                return (f"{self.nickname} has swam {self.distance} kms, and now is almost exhausted. His health is {self.health}% ")
            elif self.health >50:
                return (f"{self.nickname} has swam {self.distance} kms, but is so strong. His health is {self.health}%")
        return self

class Land(Animal):
    def __init__(self, name, nickname, size, age, health=50, happyness=50):
        super().__init__(name, nickname, size, age, health, happyness)
        self.walking = True
    
    def exercise(self, distance):
        if self.walking == True:
            self.distance = distance
            self.health -= distance
            self.happyness += distance
            if self.health <= 0:
                self.health = 0
                return (f"{self.nickname} has walked {self.distance} kms, and now is totally exhausted. His health is {self.health}%")
            elif self.health <50:
                return (f"{self.nickname} has walked {self.distance} kms, and now is almost exhausted. His health is {self.health}% ")
            elif self.health >50:
                return (f"{self.nickname} has walked {self.distance} kms, but is so strong. His health is {self.health}%")

class Sky(Animal): #not tested
    def __init__(self, name, nickname, size, age, health=50, happyness=50):
        super().__init__(name, nickname, size, age, health, happyness)
        self.flying = True
    
    def exercise(self, distance):
        if self.flying == True:
            self.distance = distance
            self.health -= distance
            self.happyness += distance
            if self.health <= 0:
                self.health = 0
                return (f"{self.nickname} has flew {self.distance} kms, and now is totally exhausted. His health is {self.health}%")
            elif self.health <50:
                return (f"{self.nickname} has flew {self.distance} kms, and now is almost exhausted. His health is {self.health}% ")
            elif self.health >50:
                return (f"{self.nickname} has flew {self.distance} kms, but is so strong. His health is {self.health}%")
            