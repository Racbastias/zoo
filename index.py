from zoo import Zoo,Animal,Food,Marines,Earthlys,Aerials

zoo = Zoo('Zoologilandia')

def Main():
    
    print(f"\nWelcome to {zoo.name}")

    while True:
        result = input ('\nWhat do yo want to do today?\n1. Create an Aerial\n2. Create an Earthly\n3. Create an Marine\n4. Feed some animal\n5. Show animals in zoo\n6. Go away\n')
        
        if result == "1":
            raza = input('¿Qué tipo de animal es?: ')
            nick = input('Póngale nombre al animal: ')
            size = input('¿Cuántos cms mide?: ')
            age = input('¿Qué edad tiene?: ')
            ave = Aerials(raza,nick,size,age,50,50)
            print('Creando Ave ... un momento')
            zoo.add_animal(ave)
            print('Agregando al zoológico\n')
            print(f"{ave.nickname} is now part of {zoo.name}!")
        
        if result == "2":
            print('We still working in this space')
            break
        if result == "3":
            print('We still working in this space')
            break
        if result == "4":
            print('We still working in this space')
            break
        if result == "5":
            print('We still working in this space')
            break
        if result == "6":
            print('¡See you later!')
            exit()
Main()
import pdb; pdb.set_trace()