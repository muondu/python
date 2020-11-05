

def adding_person():
    while True:
        try:
            Fname = input("Enter your first name:  ")
            Sname = input("Enter your second name:  ")
            Age = input("Enter your age:  ")           
        except ValueError:
            print("Sorry, I did'nt understand that")

        finally:
            print("Yay")
adding_person()


#
#def work():
#    while True:
#        try:
#            name1 = str(input("Enter yur 1 name:  "))
#            name2 = str(input("Enter yur 2 name:  "))
#            age = int(input("pls input yur age: "))
#        except ValueError:
#            print("sorry i did'nt understund that")
##            continue
#        else:
#            print(name1)
#            print(name2)
#            print(age)
#work()
#
#def video_game():
#    while True:
#        try:
#            faVideoGame = str(input("Enter yur favorite video game:  "))
#            faFood = str(input("Enter yur favorite food:  "))
#            faFruit = str(input("Enter yur favorite fruit: "))
#            faVegetable = str(input("Enter yur favorite vegatable: "))
#            faDesert = str(input("Enter yur favorite desert: "))
#            faBevarage = str(input("Enter yur favorite beverage: "))
#        except ValueError:
#            print("sorry i did'nt understund that")
##            continue
#        else:
#            print(faVideoGame)
#            print(faFood)
#            print(faFruit)
#            print(faVegetable)
#            print(faDesert)
#            print(faBevarage)
#            break
#video_game()






