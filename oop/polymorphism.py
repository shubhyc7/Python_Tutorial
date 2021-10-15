# Polymorphism
# Poly mean many and morphism mean form
# Object behave in many form / Object have many form / One thing in multiple form.
# 1. Duck Tying 
# 2. Operator Overloading
# 3. Method Overloading
# 4. Method Overring


# 1. Duck Tying- Method Behave like object / only see method available.

class PyCharm:
  def execute(self):
    print("Compliing")
    print("Runnig")


class MyEditor:
  def execute(self):
    print("Spell Check")
    print("Compliing")
    print("Runnig")


class Laptop:
  def code(self,ide):
    ide.execute()


ide = MyEditor()
# ide =PyCharm()

lap1 = Laptop()
lap1.code(ide)
 

