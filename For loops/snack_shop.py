food = {
    "Popcorn" : 10,
    "Mandazi" : 10,
   "Samosa" : 20
}
print(food)
input1 = input("How many times do you want to print it:  ")
integer = int(input1)
constructor = list()

for b in range(integer):
    input2 = food[input("Enter what you want:  ")]
    print("The price of the food is " + str(input2))
    
    
    constructor.append(input2)
    
    total = sum(constructor)
    
    
    print("Your bill is " + str(total))