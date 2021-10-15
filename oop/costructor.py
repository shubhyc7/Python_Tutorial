# conctoctor and init 
# init is constroctor


class Computer:
  def __init__(self):
    self.name = "Shubh"
    self.age = 26

  # def update(self):
  #   self.age = 25
  
  def compare(self,other):  # other is c2
    if self.age == other.age:
      return True
    else:
      return False  


c1 = Computer()
c2 = Computer()

# c1.name = "Chuadhary" 
# c1.age = 66 

# c1.update()
# print(c1.name)
# print(c1.age)

c1.age = 30
if c1.compare(c2):
  print("Same")
else:
  print("not same")
# print(id(c1))  # memory address
# print(id(c2))  # memory address
