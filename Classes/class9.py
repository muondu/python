class Person:
  def __init__(myself, name, age):
    myself.name = name
    myself.age = age

  def myfunc(kabom):
    print("Hello my name is " + kabom.name)

p1 = Person("Nesh", 11)
p1.myfunc()