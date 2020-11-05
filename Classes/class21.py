 
class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
		

python = Snake("python")
anaconda = Snake("anaconda")
print(python.name)
print(anaconda.name)