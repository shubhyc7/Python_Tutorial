# Generators
# Generators give you interator.
# Used for fetch data one by one from database without loading in memory.

# def Topten():
#    yield 5
#   # return 5

# print(Topten())


# def Topten():
#    yield 1
#    yield 2
#    yield 3
  # return 5


# val = Topten()
# print(val.__next__())
# print(val.__next__())
# print(val.__next__())
# print(next(val))


# for i in val:
#   print(i)

def Topten():
  n = 1 
  while(n<=10):
    sq = n * n
    yield sq
    n+=1


val = Topten()
for i in val:
  print(i)
