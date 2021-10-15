# Linear Search

pos = -1
def search(list, n):
  i = 0
  while i < len(list):
    if list[i] == n:
      globals() ['pos'] = i
      return True
    i = i+1
  
  return False


list = [12, 44, 66, 38, 4, 3, 83]
n = 4

if search (list, n):
  print("Found at ",pos+1)
else: 
  print("Not Found")