# Polymotphism 4

# 4. Method Overring

class A:
  def show(self):
    print("A Show")


class B(A):
  def show(self):
    print("B Show")


a1 = A()
a1.show()

b1 = B()
b1.show()  # parent class overide if we declare same method of parent class in sub class

