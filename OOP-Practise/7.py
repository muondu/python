class triange:
    def __init__(self,base,height):
        self.base = base
        self.height = height
        
    def area(self):
        formula = 0.5 * self.base * self.height
        print(formula)
        return '{},{}'.format(self.base,self.height)


base_height = triange(5,32)
triange.area(base_height)