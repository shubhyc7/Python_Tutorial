from functools import reduce 


# def is_even(n):
#   return n % 2 == 0

# num = [2,4,3,6,3,7,17,4,45,3,4]
# ev = list(filter(is_even,num))
# print(ev)


# num = [2, 4, 3, 6, 3, 7, 17, 4, 45, 3, 4]
# ev = list(filter(lambda n : n % 2 ==0, num))
# print(ev)


# def update(n):
#     return n * 2 
   
# num = [2, 4, 3, 6, 3, 7, 17, 4, 45, 3, 4]
# ev = list(filter(lambda n: n % 2 == 0, num))

# doubles = list(map(update, ev))

# print(ev)
# print(doubles)



# num = [2, 4, 3, 6, 3, 7, 17, 4, 45, 3, 4]
# ev = list(filter(lambda n: n % 2 == 0, num))

# doubles = list(map(lambda n : n * 2, ev))

# print(ev)
# print(doubles)


# def add_all(a,b):
#   return a+b

# num = [2, 4, 3, 6, 3, 7, 17, 4, 45, 3, 4]
# ev = list(filter(lambda n: n % 2 == 0, num))

# doubles = list(map(lambda n: n * 2, ev))

# sum = reduce(add_all,doubles)
# print(ev)
# print(doubles)
# print(sum)


num = [2, 4, 3, 6, 3, 7, 17, 4, 45, 3, 4]
ev = list(filter(lambda n: n % 2 == 0, num))

doubles = list(map(lambda n: n * 2, ev))

sum = reduce(lambda a, b : a + b,doubles)
print(ev)
print(doubles)
print(sum)
