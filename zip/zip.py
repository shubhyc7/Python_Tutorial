fname = {"Shubham","Tejas"}
lname = {"Chuadhary","Chuadhary"}



# zipped = zip(fname,lname)
# zippedlist = list(zip(fname,lname))
# zippedset = set(zip(fname,lname))
# zippeddict = dict(zip(fname,lname))

print(fname)
print(lname)
# print(zipped)

# print(zippedlist)
# print(zippedset)
# print(zippeddict)


zipped = zip(fname, lname)
for (a,b) in zipped:
  print(a,b)