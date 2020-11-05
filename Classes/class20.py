class Snake:
	name = "python"
	
	
	
	def change_name(self, new_game):
		self.name = new_game
		
snake = Snake()

print(snake.name)



snake.change_name("Anaconda")
print(snake.name)