#data type, data structures, sequence prg
datalist = [43, 55, 200]
print(type(datalist))


fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
# fruits.clear()
print(fruits)

x = fruits.count("cherry")
print(x)
cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)

x = fruits.index("cherry")
print(x)

fruits.insert(1, "orange")
print(fruits)
fruits.pop(1)
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.reverse()
print(fruits)

cars.sort()
print(fruits)
cars.sort(reverse=True)
print(fruits)
