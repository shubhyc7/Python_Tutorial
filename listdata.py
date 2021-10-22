'''

Python Data Structures (built-in collection data types)- Lists, Tuples, Sets, Dictionaries

List :  
  * Lists are used to store multiple items in a single variable.

  * List items are ordered, changeable, and allow duplicate values.

  * A list can contain different data types.
  
  * e.g.
      fruits = ['apple', 'banana', 'cherry']
      cars = ['Ford', 'BMW', 'Volvo']
      thislist = list(("apple", "banana", "cherry"))

  Method :  
    1. fruits.append("orange")
    2. fruits.clear()
    3. x = fruits.copy()
    4. x = fruits.count("cherry") 
    5. fruits.extend(cars)
    6. x = fruits.index("cherry")
    7. fruits.insert(1, "orange")
    8. fruits.pop(1)
    9. fruits.remove("banana")
   10. fruits.reverse()
   11. cars.sort()

'''


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
