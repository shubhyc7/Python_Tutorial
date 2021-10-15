# Binary Search - In the binary search values are  Increasing Order Sorted.

pos = -1

def search(list, n):
  
  l = 0
  u = len(list) - 1

  while l <= u:
    m = (l + u) // 2

    if list[m] == n:
      globals()['pos'] = m
      return True
    
    else:
      if list[m] < n:
        l = m + 1
      else:
        u = m - 1  
    
  return False  



list = [4,7,8,12,45,99]
n = 77

if search(list, n):
  print("Found at ", pos+1)
else:
  print("Not Found")
