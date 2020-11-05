class Name:
	
	def __init__(self, age):
		self.age = age
		
		
	def say_age(self):
		print("My age is ",self.age)
		
p = Name(11)
p.say_age()