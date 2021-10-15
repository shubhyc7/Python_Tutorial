class A:
  def featureA1(self):
    print("Feature A1")
  
  def featureA2(self):
    print("Feature A2")


class B(A):
  def featureB3(self):
    print("Feature B3")
  
  def featureB4(self):
    print("Feature B4")


class C(B):
  def featureC5(self):
    print("Feature C5")

class D:
  def featureD6(self):
    print("Feature D6")

class E(A,D):
  def featureE7(self):
    print("Feature E7")

# a1 = A()    
# a1.featureA1()
# a1.featureA2()

# b1 = B()  #Single
# b1.featureA1()
# b1.featureA2()
# b1.featureB3()
# b1.featureB4()


# c1 = C()  # Multilevel
# c1.featureA1()
# c1.featureA2()
# c1.featureB3()
# c1.featureB4()
# c1.featureC5()


e1 = E()  # Multiple
e1.featureA1()
e1.featureA2()
e1.featureD6()
e1.featureE7()
