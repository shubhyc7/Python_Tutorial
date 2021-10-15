# Iterator -  ++  which means iteration 
# Intertaot - Used to fetch one value at a time /  Fetch one by one
# lst = [24,68,63,46,78]

# # print(lst[3])

# # for i in lst:
# #   print(i)

# it = iter(lst)
# # print(it.__next__())
# # print(it.__next__())
# # print(next(it))
# # print(next(it))

# for i in lst:
#   print(i)



class Topten:
  def __init__(self):
    self.num = 1

  def __iter__(self):
    return  self

  def __next__(self):

    if self.num <= 10:
      val = self.num
      # self.num = self.num +1
      self.num +=1

      return val 
    else:
      raise StopIteration


val = Topten()


# print(val.__next__())
print(next(val))

for i in val:
  print(i)


