'''

Sets : 
  * Sets are used to store multiple items in a single variable.
  * A set is a collection which is unordered, unchangeable, and unindexed.
  * Duplicates Not Allowed.
  * A set can contain different data types.


  * e.g.
      thisset = {"apple", "banana", "cherry", "apple"}
      set1 = {"abc", 34, True, 40, "male"}
      thisset = set(("apple", "banana", "cherry"))

  Method :
    1. thisset.add("orange")
    2. thisset.clear()
    3. x = fruits.copy()
    4. z = x.intersection(y) 
    5. z = x.issubset(y) 
    6. z = x.issuperset(y)
    7. z = x.union(y) 
    8. x.update(y) 
    9. fruits.remove("banana") 
   10.  fruits.pop()


'''


#data type, data structures, sequence prg
dataset = {56, 30, 45}
print(type(dataset))
dataset.add(66)
# dataset.clear()
x = dataset.copy()
print(x)

dataset.pop()
dataset.remove(45)
print(dataset)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)
print(z)
