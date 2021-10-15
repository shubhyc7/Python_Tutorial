# Polymotphism 3

# 3. Method Overloading - Not in python

class Student:
  def __init__(self,m1,m2):
    self.m1 = m1
    self.m2 = m2

  def sum(self, a=None, b=None, c=None):
    s = 0
    if a != None and b != None and c != None:
      s = a+b+c
    
    elif a != None and b != None:
      s = a+b

    elif a != None:
      s = a
    
    else:
      s = 'ss'
    
    return s


s1 = Student(11,1)

print(s1.sum(1,2,3))
print(s1.sum(1,2))
print(s1.sum(1))
print(s1.sum())
