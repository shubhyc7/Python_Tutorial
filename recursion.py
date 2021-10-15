# import sys

# sys.setrecursionlimit(1500)
# print(sys.getrecursionlimit())

# i = 1
# def abc():
#   global i
#   i+=1 
#   print('Hello',i)
#   abc()


# abc()  


# fact using recursion


def fact(n):
  if n==0:
    return 1
  r =  n * fact(n-1)
  return r 

x= fact(5)
print(x)


# 5 * 4
# 4 * 3
# 3 * 2
# 2 * 1
# 1 * 0
