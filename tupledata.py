'''

Tuples :
  * Tuples are used to store multiple items in a single variable.
  * A tuple is a collection which is ordered and unchangeable.
  * Tuple items are ordered, unchangeable, and allow duplicate values.
  * A tuple can contain different data types.

  * e.g.
      thistuple = ("apple", "banana", "cherry")
      thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
      thistuple = tuple(("apple", "banana", "cherry"))

  Method :
    1. x = thistuple.count(5)
    2. x = thistuple.index(8)


'''

#data type, data structures, sequence prg
datatup = (40, 30, 300)
print(type(datatup))


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
