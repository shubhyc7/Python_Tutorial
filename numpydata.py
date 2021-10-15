# for miltiple dimention array used numpy
from numpy  import *

# arr = array([1,3,2,4,4,4,4])
# arr = array([1,3,2,4,4,4,4],int)
# print(arr)

# arr = array([1, 3, 2, 402.3, 4, 4, 4],float)
# print(arr)
# print(arr.dtype)

# arr = linspace(1,49,7)
# print(arr)

# arr = arange(0, 11, 2)
# print(arr)

# arr = logspace(1, 40, 5)
# print(arr)
# print('%.2f' %arr[4])

# arr = linspace(1, 11, 2)
# print(arr)


# arr = array([1,2,3,4,1,4])
# brr = array([1,2,3,4,1,4])
# crr = arr + brr
# print(crr)


# arr = array([1, 2, 3, 4, 1, 4])
# crr = arr + 4
# print(crr)


# arr = array([1, 2, 3, 4, 1, 4])
# brr = array([1, 2, 3, 4, 1, 4])
# print(log(arr))
# print(cos(arr))
# print(sqrt(arr))
# print(sum(arr))
# print(min(arr))
# print(max(arr))

# print(concatenate([arr,brr]))


# arr = array([1, 2, 3, 4, 1, 4])
# # brr = arr
# # print(arr)
# # print(brr)
# # print(id(arr))
# # print(id(brr))

# brr = arr.view  #value of b is change if change the value of a that shalow copy

# arr[1] = 7 
# print(brr)
# print(id(arr))
# print(id(brr))


arr = array([1, 2, 3, 4, 1, 4])
brr = arr.copy()  # deep copy

arr[1] = 7  

print(arr)
print(brr)

print(id(arr))
print(id(brr))



