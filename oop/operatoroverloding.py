# Polymorphism 2

# 2. Operator Overloading
# a = 5
# b = 6

# print(a + b)
# print(int.__add__(a,b)) #add sub mul div magic method

# a = 'ss'
# b = 'dd'
# print(a + b)
# print(str.__add__(a, b))


class Student:
  def __init__(self,m1,m2):
    self.m1 = m1
    self.m2 = m2

  def __add__(self,other):
    m1 = self.m1 + other.m1  
    m2 = self.m2 + other.m2  
    s3 = Student(m1,m2)
    return s3

  def __gt__(self,o):
    r1 = self.m1 + self.m2
    r2 = o.m1 + o.m2
    if r1 > r2:
      return True
    else:
      return False  

  def __str__(self):
    return '{} {} '.format(self.m1, self.m2)



s1 = Student(35,35) #70
s2 = Student(30,35) #65

s3 = s1 + s2

print(s3.m1)
print(s3.m2)


if s1 > s2:
  print("S1 Wins")
else:
  print("S2 Wins")  

# print(s1)
# print(s1.__str__())
print(s1)
print(s2)
