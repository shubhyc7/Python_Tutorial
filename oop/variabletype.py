# instance variable and class variable (static variable)

class Car:

  wheels = 4 #access with object as well as clss name  Class Variable Static Variable
  def __init__(self):
    self.mil = 10 #instance variable
    self.com = "BMW"



c1 = Car()
c2 = Car()

c1.mil = 8
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)

Car.wheels = 6

print(c1.mil, c1.com, Car.wheels) 
print(c2.mil, c2.com, Car.wheels)
