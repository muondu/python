
class Employee:
    def __init__(self,first,last,pay,email):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = email


    def full_imformation(self):
        return '{} {} {} {}'.format(self.first,self.last,self.pay,self.email)

# print(emp1.full_imformation())
# print(Employee.full_imformation(emp1))
# print(Employee(emp1))


