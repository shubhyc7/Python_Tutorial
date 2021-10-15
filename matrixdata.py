# Multi dimention array
from numpy import *

arr = array([
        [13,12,13,54,2,5],
        [45,67,44,6,33,2]
      ])

# print(arr)
# print(arr.dtype)
# print(arr.ndim)
# print(arr.shape)
# print(arr.size)


# brr = arr.flatten() #coversion flat arrat to one dimension
# print(brr)

brr = arr.flatten()
# crr = brr.reshape(4,3)
# print(crr)


# crr = brr.reshape(2,2,3)
# print(crr)


# crr = brr.reshape(1, 2, 6)
# print(crr)


# m = matrix(arr)
# print(m)



# m = matrix('1 2 3 ; 4 1 2 ; 3 4 5')
# print(m)

# print(diagonal(m))
# print(m.min())
# print(m.max())


m1 = matrix('1 2 3 ; 4 1 2 ; 3 4 5')
m2 = matrix('1 2 3 ; 4 1 2 ; 3 4 5')
print(m1)
print(m2)
m3 = m1 * m2
print(m3)
