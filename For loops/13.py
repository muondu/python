
cars = {
    "Probox" : 5000,
    "Land cruiser" : 8000,
   "BMW" : 7000
}
print(cars)
input1 = input("How many times do you want to print it:  ")
integer = int(input1)
constructor = list()

for c in range(integer):
    input2 = cars[input("Enter what car you want:  ")]
    print("The price of the car is " + str(input2))
    
    
    constructor.append(input2)
    
    total = sum(constructor)
    
    
    print("Your biill of the cars is  " + str(total))