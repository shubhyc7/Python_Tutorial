class Student:
  def __init__(self, name,rno):
    self.name = name
    self.rno = rno
    self.lap = self.Laptop()

  def show(self):
    print(self.name, self.rno)
    self.lap.show()

  class Laptop:
    def __init__(self):
      self.brand = 'HP'
      self.cpu = 'i3'
      self.ram = '4'

    def show(self):
      print(self.brand, self.cpu, self.ram)

  
s1 = Student('ddd',21)
s2 = Student('ee',24)


# s1.show()
# s2.show()


# lap1 = s1.lap
# lap2 = s2.lap

# print(id(lap1))
# print(id(lap2))

s1.show()