class employee:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay

    def lola(self):
        return '{} {}'.format(self.name,self.pay)
        