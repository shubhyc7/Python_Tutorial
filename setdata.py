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
