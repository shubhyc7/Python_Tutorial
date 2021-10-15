class Computer:
  def __init__(self,cpu,ram):
    self.cpu = cpu
    self.ram = ram

  def config(self):
    print("64 GB,4 GB RAM")
    print("Config is",self.cpu,self.ram)


# com1 = Computer()
# com2 = Computer()
# Computer.config(com1) #com1 this is third arg
# Computer.config(com2)

com1 = Computer('i5',16)
com2 = Computer('i7',32)

com1.config()
com2.config()


