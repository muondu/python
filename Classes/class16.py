class Person:
	def __init__(dub,name, age):
		dub.name = name
		dub.age = age
		
	def myfunc(abc):
		print("Hello my name is " + abc.name)
		
		
p1 = Person("Munene", 12)
p1.myfunc()