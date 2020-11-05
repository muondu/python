class Vehicle_Car:
    def __init__(self,name,capacity,milage):
        self.name = name
        self.capacity = capacity
        self.milage = milage
    def fair(self):
        return self.capacity * 100
class Bus(Vehicle_Car):
    def fair(self):
        amount = super().fair()
        amount += amount * 10 / 100
        return amount
    

bus = Bus('Nero Nesh',50,100000)
# print(bus.fair())



class Student:
    def __init__(self,name,std):
        self.name = name
        self.std = std  
    
    def display(self):
        return "Full names are {} and class is {}".format(self.name,self.std)

class Manager(Student):
    def __init__(self,name,std,age = None, marks = None):
        Student.__init__(self,name,std)

        if age is None:
            self.age = []
        else:
            self.age = age
        if marks is None:
            self.marks = []
        else:
            self.marks = marks
    def add_ifmromation(self,student):
        if student not in self.age:
            self.age.append(student)
            if student not in self.marks:
                self.age.append(student)

st1 = Student('Nesh',7)

mng = Manager('Nero Nesh',7,11,100)

mng.add_ifmromation(mng)