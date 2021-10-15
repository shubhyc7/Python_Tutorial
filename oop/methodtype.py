#Methods Types (Fuctions in oop class methods)

class Student:

  school = "Telusko"

  def __init__(self,m1,m2,m3):
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3

  def avg(self):
    return (self.m1 + self.m2 + self.m3) / 3

  def get_m1(self):  # accessor method - for access
    return self.m2

  def set_m1(self, value):  # Mutator method - for update
    self.m1 = value

  @classmethod
  def getSchool(cls):
    return cls.school

  @staticmethod
  def info():
    print("This is Student Class")

s1 = Student(23,42,35)    
s2 = Student(21,12,45)    

# print(s1.avg())
# print(s2.avg())
# print(Student.school)
# print(s1.info())
# print(Student.getSchool())

print(Student.info())


# accessor method - for access
# Mutator method - for update
