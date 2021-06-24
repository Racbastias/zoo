from zoo import Zoo,Animal, Food, Foods, Water, Land, Sky

#Variable Zoologico
zoo = Zoo('Zoologilandia')

#Variable Comida
food = Food('food')

#Variable Comida
zanahoria = Foods('Zanahoria', 10, 10)
pescado = Foods('Pescado', 20, 10)
parrillada = Foods('Parrillada', 30, 10)
papasfritas = Foods('Papas Fritas', -30,20)
plastico = Foods('Bolsa Plástica', -30, -30)
superocho = Foods('Super Ocho', -10,10)

#Integración comidas
food.add_food(zanahoria)
food.add_food(pescado)
food.add_food(parrillada)
food.add_food(papasfritas)
food.add_food(plastico)
food.add_food(superocho)

def Main():
    
    print(f"\nWelcome to {zoo.name}")

    while True:
        result = input ('\nWhat do yo want to do?\n\n1. Create an Water Animal\n2. Create an Land Animal\n3. Create an Sky Animal\n4. Feed some Animal\n5. Do some exercise\n6. Show animals in zoo\n7. Go away\n')
        
        if result == "1":
            name = input('\nWhat kind of animal is?: ')
            nickname = input('what is the name?: ')
            size = input('How many cms of lenght is this animal?: ')
            age = input('How old is?: ')
            zoo.add_water(name, nickname, size, age)
            print(f"\nCongratulations! {nickname} is now at the zoo.\nWhat would you do now?:")
            continue
        
        elif result == "2":
            name = input('\nWhat kind of animal is?: ')
            nickname = input('what is the name?: ')
            size = input('How many cms of lenght is this animal?: ')
            age = input('How old is?: ')
            zoo.add_land(name, nickname, size, age)
            print(f"\nCongratulations! {nickname} is now at the zoo.\nWhat would you do now?:")
            continue
        elif result == "3":
            name = input('\nWhat kind of animal is?: ')
            nickname = input('what is the name?: ')
            size = input('How many cms of lenght is this animal?: ')
            age = input('How old is?: ')
            zoo.add_sky(name, nickname, size, age)
            print(f"\nCongratulations! {nickname} is now at the zoo.\nWhat would you do now?:")
            continue
        elif result == "4":
            print('\nWhat animal do you want to feed?: ')
            for i in range (0, len(zoo.animals)):
                print(i, '- ',zoo.animals[i].nickname)
            choice = int(input('Please write the number of the animal here: '))
            print(f"\nYou choose {zoo.animals[choice]}")
            print(f"\nChoose the food you want to give to {zoo.animals[choice].nickname}: ")
            for i in range (0,len(food.foods)):
                print(i, '- ', food.foods[i])
            select = int(input('\nPlease write the number of the option: '))
            animal = zoo.animals[choice]
            foody = animal.feed(food.foods[select])
            print(foody)
            continue
        elif result == "5":
            print('\nWhat animal do you want to exercise?: ')
            for i in range (0, len(zoo.animals)):
                print(i, '- ',zoo.animals[i].nickname)
            choice = int(input('Please write the number of the animal here: '))
            print(f"\nYou choose {zoo.animals[choice].nickname} the {zoo.animals[choice].name}")
            distance = int(input(f"\nHow many kilometers you wanna try with {zoo.animals[choice].nickname}?: "))
            animal = zoo.animals[choice]
            exercise = animal.exercise(distance)
            print(exercise)
            continue
        elif result == "6":
            print('\n', zoo.zoo_information())
            continue
        elif result == "7":
            print('\n¡See you later!\n')
            exit()
        else:
            print('Please write a valid answer')
            continue

Main()
import pdb; pdb.set_trace()
