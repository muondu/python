
class  Employee:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        
    def names(self):
        return " full names {}{}".format(self.fname,self.lname)

class Manager(Employee):
    def __init__(self,fname,lname,salary,employees = None):
        Employee.__init__(self,fname,lname,salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees  
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_names(self):
        for employe in self.employees:
            print("-->",employe.names())


m1 = Manager('Nero','Nesh',1000000000000)

m1.add_emp(m1)
# print(m1.employees)
m1.print_names()










# class Car:
#     def __init__(self,name,colour,price):
#         self.name = name
#         self.colour = colour
#         self.price = price

#     def carol(self):
#         return "{} {} {}".format(self.name,self.colour,self.price)

# class Manager_cars(Car):
#     def __init__(self,name,color,price,model=None):
#         Car.__init__(self,name,color,price)
#         if model is None:
#             self.model = []
#         else:
#             self.model = model  

#         def add_mdl(self,mdl):
#         if mdl not in self.model:
#             self.model.append(mdl)

#     def remove_mdl(self,mdl):
#         if mdl in self.model:
#             self.model.remove(mdl)

#     def print_models(self):
#         for models in self.model:
#             print("-->",models.carol())

# mn_car = Manager_cars('Toyota','Nesh',"Red",1000000000000)

# print(mn_car.name)


# car1 = Manager_cars('Toyota','Nesh',"Red",1000000000000)
# car2 = Car('Voxwagen','Malli',"Blue",1000000000000,)
# print(car1.carol())



# class  Customer:
#     def __init__(self,fname,lname,payment):
#         self.fname = fname
#         self.lname = lname
#         self.payment = payment
#     def imformation(self):
#         return "{} {} {}".format(self.fname,self.lname,self.payment)



# class Developer(Employee):
#     def __init__(self,fname,lname,salary,programing_language):
#         Employee.__init__(self,fname,lname,salary)
#         self.programing_language = programing_language

# dev1 = Developer('Nero','Nesh',10000000,"Python")
# dev2 = Developer('Malli','Muondu',10000000,"Java")
# # print(dev1.programing_language)

# # print(m1.employees)
# # m1.print_names()






# # emp1 = Employee('Nero','Nesh',10000000000)

# # car1 = Car('NERO NESH','Orange',1000000000000000000000000000)

# # customer1 = Customer("Nero","Nesh",1000000000000000000000000000)
# # print(emp1.names())
# # print(car1.carol())

# # print(customer1.imformation())
