
# Even and odd using list


def count(lst):
  e = 0
  o = 0

  for i in lst:
    if i % 2 == 0:
      e += 1
    else:
      o += 1
  return e, o


lst = [18,55,32,45,68,96,42,47]
even, odd = count(lst)

print(even)
print(odd)
print(even,odd)
print("Even : {} and Odd : {}".format(even,odd))
