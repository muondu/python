print("Write names of trees")

a = []

b = a.append(input("Enter your first sentence:  "))
print(a)
c = a.append(input("Enter your second sentence:  "))
print(a)
d = a.append(input("Enter your third sentence:  "))
print(a)
e = a.append(input("Enter your fourth sentence:  "))
print(a)
f = a.append(input("Enter your fifth sentence:  "))
a.sort()
a.pop()
a.remove(input("Remove any word in our list:  "))
print(a)

print("Write names of flowers")
g = []
h = g.append(input("Enter your first sentence:  "))
print(g)
i = g.append(input("Enter your second sentence:  "))
print(g)
j = g.append(input("Enter your third sentence:  "))
print(g)
k = g.append(input("Enter your fourth sentence:  "))
print(g)
l = g.append(input("Enter your fifth sentence:  "))
g.sort()
g.pop()
g.remove(input("Remove any word in our list:  "))

print(g)