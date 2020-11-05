class Students:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def imformation(self):
        return "Full names and class {}{}".format(self.fname,self.lname)



# print(std1.imformation())


class Manager(Students):

    def __init__(self,fname,lname,classe=None):

        Students.__init__(self,fname,lname)

        if classe is None:
            self.classe = []
        else:
            self.classe = classe

    def add_student(self,student):  
        if student not in self.classe:
            self.classe.append(student)

    def remove_student(self,student):
        if student not in self.classe:
            self.classe.remove(student)

    def print_students(self):
        for students in self.classe:
            print("--> ",students.imformation())

std1 = Students('nesh','wolf')
    
mng = Manager('newton', 'adams')

mng.add_student(std1)

print(mng.classe)

