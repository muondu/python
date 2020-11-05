 
fruits = {
    "Apple" : 30,
    "Banana" : 10,
   "Pineaple" : 70
}
print(fruits)
input1 = input("How many times do you want to print it:  ")
integer = int(input1)
constructor = list()

for b in range(integer):
    input2 = fruits[input("Enter what you want:  ")]
    print("The price of the fruit is " + str(input2))
    
    
    constructor.append(input2)
    
    total = sum(constructor)
    
    
    print("Your total is " + str(total))