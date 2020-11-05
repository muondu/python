class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        formula = 3.142 * self.radius * self.radius
        print(formula)
        return '{}'.format(self.radius)

dub = Circle(7)
Circle.area(dub)