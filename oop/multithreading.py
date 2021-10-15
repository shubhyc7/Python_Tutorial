# Multithreading


# class Hello:
#   def run(self):
#     for i in range(5):
#       print("Hello")

# class Hi:  
#   def run(self):
#     for i in range(5):
#       print("Hi")

# h1 = Hello()
# h2 = Hi()

# h1.run()
# h2.run()

from threading import *
from time import sleep 


class Hello(Thread):
  def run(self):  # run is inbuilt method 
    for i in range(5):
      print("Hello")
      sleep(1)

class Hi(Thread):
  def run(self):
    for i in range(5):
      print("Hi")
      sleep(1)

h1 = Hello()
h2 = Hi()

# h1.run()
# h2.run()

h1.start()
sleep(0.2)
h2.start()


h1.join()
h2.join()
print('Bye')
