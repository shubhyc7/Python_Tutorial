# def abc():
#   print("Hello this a fuction")

# abc()


# def abc():
#   return "Hello"

# print(abc())


# def adddata(x,y):
#   return x+y

# print(adddata(4,5))


# def adddata(x, y):
#   z = x + y
#   print(z)

# adddata(4, 5)


def update(x):
  x = 8
  print(x)

#no call by value and no call by reference in python. if we pass value it id has same and if we update it value the id is change(id means reference).
# a = 10  
# update(a)
# print(a)
# print("a :", a)


# def update1(x):
#   print(id(x))
#   x = 10
#   print(id(x))
#   print(x)
#   print("x :", x)

# a = 10
# print(id(a))
# update1(a)
# print(id(a))
# print(a)
# print(id(a))
# print("a :", a)

# def adddata(x):
#   print(id(x))
#   print("x :", x)

# a = 10
# print(id(a))
# adddata(a)
# print("a :", a)


# def uplist(lst):
#   lst[1]=55
#   print(id(lst))
#   print("lst :", lst)

# lst = [12,112,234]
# print(id(lst))
# uplist(lst)
# print("lst :", lst)



# def addfun(a,b):
#   c = a + b
#   print(c)

# addfun(5,4)


# def person(name, age):
#   print(name)
#   print(age)

# person('aaa',18)


# def person(name, age):
#   print(name)
#   print(age-2)
# person('aaa', 18)
# person(name='aaa', age=18)


# def person(name='', age=18):  # degault arg
#     print(name)
#     print(age)

# person('aaa')
# person()


# def sum(a,*b):   # variable legth arg
#     c = a
    
#     for i in b:
#        c = c+ i

#     print(c)


# sum(10,20,20,20)


# def sum(*b):  # variable legth arg
#     c = 0
#     for i in b:
#        c = c + i

#     print(c)


# sum(10, 20, 20, 20)


# def person(name, *data):
#   print(name)
  
#   print(data)


# person('abc',23,'nashik',12121121211)


# def person(name, **data):  # keyworded variable length arg **kwargs
#   print(name)
#   print(data)
#   print(data['age'])

# person('abc', age=23, city='nashik', mob=12121121211)


# def person(name, **data):  # keyworded variable length arg **kwargs
#   print(name)
#   for i,j in data.items():
#     print(i,j)

# person('abc', age=23, city='nashik', mob=12121121211)


# a = 10  # Global Keyword

# def something():
#   a = 15 # local variable
#   b = 20 
#   print('in fun :',a)
#   # print(b)

# something()

# print('outside :',a)
# print(b)


# a = 10  # Global Keyword


# def something():
#   print('in fun :', a)
  

# something()

# print('outside :', a)


a = 10  # Global Keyword


# def something():
#   global a # to change value of global outside variable value
#   a =15
#   print('in fun :', a)


# something()

# print('outside :', a)


a = 10
print(id(a))

def something():
  a = 15
  x = globals() ['a']

  print(id(x))
  print('in fun :', a)

  globals() ['a'] = 20

something()

print('outside :', a)
