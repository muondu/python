# Python program to 
# demonstrate init with 
# inheritance 

class A(object): 
	def __init__(self, something): 
		print("Hello Malli") 
		self.something = something 
		

class B(A): 
	def __init__(self, something): 
		# Calling init of parent class 
		A.__init__(self, something) 
		print("Hello nesh") 
		self.something = something 
		
obj = B("Something") 