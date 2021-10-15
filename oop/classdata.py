class Computer:
  def config(self):
    print("64 GB,4 GB RAM")


a = 5
print(type(a))

s = '5'
print(type(s))

com1 = Computer()
com2 = Computer()
# print(type(com1))

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()

a=5
a.bit_length()
print(a)
print(a.bit_length())