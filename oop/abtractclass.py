# Abtract Class

# Python by default not support abtract class

# Abtract Class - Method Only has declaration but defination (empty method)

# You can not create object of abstract class
# ---------------Other Laguage----------------------------------
# class Comp: #class has abtract method is abtract class
#   def process(self):  # abtract method
#     pass


# c = Comp()
# c.process()
# --------------------------------------------------------------
from abc import ABC,abstractmethod  # ABC - Abstract Base Class


class Comp(ABC): 
  @abstractmethod 
  def process(self):
    print("This is Comp Method")


class Laptop(Comp): 
  def process(self):
    print("This is Laptop Method")


class Prog:
  def work(self,com):
    print("Solve Bugs")
    com.process()


# class whiteboard(Comp):
#   def write(self):
#     print('Writing')

# c = Comp()
# c.process()

# l = Laptop()
# l.process()

l = Laptop()
pr = Prog()
pr.work(l)

# w = whiteboard()
# pr = Prog()
# pr.work(w)
