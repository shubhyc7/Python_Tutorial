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
