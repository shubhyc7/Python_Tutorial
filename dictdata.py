'''

Dictionaries : 
  * Dictionaries are used to store data values in key:value pairs.
  * A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
  * Dictionaries cannot have two items with the same key:
  * The values in dictionary items can be of any data type:

  * e.g.
      thisdict =	{ "brand": "Ford", "model": "Mustang", "year": 1964 }
      thisdict["brand"]
      Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
      car =	{"brand": "Ford","model": "Mustang", "year": 1964 }
      x = ('key1', 'key2', 'key3')
      y = 0

  Method :
    1. car.clear()
    2. x = car.copy()
    3. thisdict = dict.fromkeys(x, y)
    4. x = car.get("model")
    5. x = car.items()
    6. car.popitem()
    7. x = car.setdefault("model5", "Bronco")
    8. car.update({"color": "White"})
    9. x = car.values()


'''


#data type, data structures, sequence prg
datadict = {1:'aa', 2:'bb', 'abc':'abcabc'}
print(type(datadict))
print(datadict.keys())
print(datadict.values())


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.clear()

print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# car.clear()

print(car)

x = car.copy()

print(x)


x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)


y = car.get("model")

print(y)

x = car.items()

car.pop("model")
car.popitem()
car.update({"color": "White"})
print(x)
