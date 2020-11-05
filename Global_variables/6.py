c = 0

def add():
	global c
	c = c + 2
	print("Inside add():",c)
	
add()
print("In the main:",c)