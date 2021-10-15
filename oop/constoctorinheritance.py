class A:
  def __init__(self):
    print("Construror of A")

  def featureA1(self):
    print("Feature A1")

  def featureA2(self):
    print("Feature A2")


class B(A):
  def __init__(self):
    super().__init__()
    print("Construror of B") # First call subclass constructor
    super().__init__()

  def featureB3(self):
    print("Feature B3")

  def featureB4(self):
    print("Feature B4")


class D:
  def __init__(self):
    print("Construror of D")
    
  def featureD6(self):
    print("Feature D6")

  def featureA1(self):
    print("Feature A1 for MRO")


class E(A, D): 
  def __init__(self):
    super().__init__()   # class E(A, D) left to right order
    print("Construror of E")  # First call subclass constructor
    
  def featureE7(self):
    print("Feature E7")

  def feat(self):
    super().featureA1()
  
# b1 = B()
# b1.featureA1()
# b1.featureA2()
# b1.featureB3()
# b1.featureB4()

# MRO - Method Resolution Order
e1 = E()  # Multiple   
e1.featureA1()
e1.featureA2()
e1.featureD6()
e1.featureE7()


e1.feat()