#Import time
import time
a = "Opps! We have an unwanted word in our list"
print(a)
b = ["Bugatti","Jaguar","BMW","Cow","Subaru"]
print(b)       
c = "Let as remove the unwanted word in our list: "
print(c)

time.sleep(1)

d = b.remove(input("Enter the wrong one:  "))

time.sleep(1)

print(b)

e = b.append(input("Enter the write thing:  "))
time.sleep(1)
print(b)
f = b.insert(5, "Lamboghini")
time.sleep(2)
b.sort()
time.sleep(1)
g = len(b)
print(b)


print("This program will put what three things that you have written in a list")
h = []
i = h.append(input("Enter your first word:  "))
print(h)
j = h.append(input("Enter your second word:  "))
print(h)
k = h.append(input("Enter your third word:  "))
print(h)

l = b + h
print(l)