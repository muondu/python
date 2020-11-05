def trirecrution(k):
    if(k>0):
        result = k + trirecrution(k - 1)
        print(result)
    else:
        result = 0
        return result
print("\n\nRecursion Example Results")
trirecrution(6)