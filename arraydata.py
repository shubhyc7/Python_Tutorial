from array import *
# import array as a

# a = array('i',[2,3,4,5])
# print(a)

# # a = array('I', [2, -3, 4, 5])
# # print(a)

# print(a.buffer_info())
# a.reverse()
# print(a)

# print(a[0])

# for i in a:
#   print(i)

# for i in range(0):
#   print(a[i])


# unichar = ('u',['a','s','d','d'])  
# print(unichar)


a = array('i',[2,3,4,5])

# newa = array(a.typecode,(i for i in a))
# # print(newa)

# for n in newa:
#   print(n)


# a = array('i', [2, 3, 4, 5])

# newa = array(a.typecode, (i*i for i in a))
# # print(newa)

# for n in newa:
#   print(n)


# i=0;
# while i < len(a):
#     print(a[i])
#     i=i+1
# print(newa)


# fruits = ['apple', 'banana', 'cherry']
# fruits.append("orange")
# print(fruits)


# fruits = ['apple', 'banana', 'cherry', 'orange']

# fruits.clear()
# print(fruits)


# fruits = ['apple', 'banana', 'cherry', 'orange']

# x = fruits.copy()
# print(x)


# fruits = ['apple', 'banana', 'cherry']

# x = fruits.count("cherry")
# print(x)


# fruits = ['apple', 'banana', 'cherry']

# cars = ['Ford', 'BMW', 'Volvo']

# fruits.extend(cars)
# print(fruits)


fruits = ['apple', 'banana', 'cherry']

# x = fruits.index("cherry")
# print(x)


# fruits.insert(1, "orange")
# fruits.pop(1)
# fruits.remove("banana")
# fruits.reverse()
# print(fruits)


# cars = ['Ford', 'BMW', 'Volvo']

# cars.sort()
# print(cars)


arr = array('i',[])
n = int(input("Enter Length :"))

for i in range(n):
  x = int(input("Enter Value :"))
  arr.append(x)

print(arr)


val = int(input("Enter Value to search:"))
k=0
for e in arr:
  if e == val:
    print(k)
    break
  k+=1
else:
  print("not found")


print(arr.index(val))