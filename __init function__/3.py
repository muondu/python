class Person: 
	
	def __init__(self,name): 
		self.name = name 
	# Sample Method 
	def say_hi(self): 
		print('Hello, my name is', self.name)  

# Creating different objects	 
p1 = Person('Munene') 
p1.say_hi() 