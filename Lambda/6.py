def lambdafunction(n):
	return lambda a : a * n
mydoubler = lambdafunction(3)
print(mydoubler(4))