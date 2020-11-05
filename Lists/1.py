print("Write names of cars")

a = []

b = a.append(input("Enter your first sentence:  "))
print(a)
c = a.append(input("Enter your second sentence:  "))
print(a)
d = a.append(input("Enter your third sentence:  "))
print(a)
e = a.append(input("Enter your fourth sentence:  "))
print(a)
f = a.append(input("Enter your fifth sentence:   "))
a.sort()
a.pop()
a.remove(input("Remove a word in the list:  "))  
print(a)
print("Write names of people")
g = []
h = g.append(input("Enter your first sentence:  "))
print(g)
i = g.append(input("Enter your second sentence:  "))
print(g)
j = g.append(input("Enter your third sentence:  "))
print(g)
k = g.append(input("Enter your fourth sentence:  "))
print(g)
l = g.append(input("Enter your fifth sentence:   "))
g.sort()
g.pop()
g.remove(input("Remove a word in the list:  "))

print(g)


list1 = a + g
print(list1)

