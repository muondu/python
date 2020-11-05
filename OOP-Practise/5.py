class Students:
    def __init__(self,first,last,grade):
        self.first = first
        self.last = last
        self.grade = grade

    def imformation(self):
        # return '{} {} {}'.format(self.first,self.last,self.grade)
        return '{}'.format(self.first[::-1])
student1 = Students('Newton','Adams',9)
student2 = Students('Frank','Tamre',9)
print(Students.imformation(student1))