cars = {
    "milk" : 50,
     "bread" : 55
}
d = int(input("whow many times do you want to print: "))# this asks you whaw many times do you want to print
e = list() 

for c in range(d):
    f = cars[input ("write what you want to select: ")]
    g = e.append(f)
    
    total = sum (e)
   

    
    print("price is " + str(f))
    
    print("total amount to pay is " + str(total))
    
    
    
   