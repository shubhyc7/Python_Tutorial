# Exception handling

# Means Error handing

# Type of error :
# 1. Compile time error - Syntax Error
# 2. Logical error - Answer is wrong
# 3. Runtime error - If the given input is wrong
# ----------------------------------------------

a = 5
# b = 2
b = 0

# try:
#   c = a / b
#   print(c)
# except Exception:
#   print("You Can not Divide by Zero")

# print("Bye")

# try:
#   c = a / b
#   print(c)
# except Exception as e:
#   print("Exception :",e)

# print("Bye")

# a = 5
# b = 2

# try:
#   print("open")
#   c = a / b
#   print(c)
#   # print("close")

# except Exception as e:
#   print("Exception :", e)
#   # print("close")
# finally:
#   print("close")
# print("Bye")

a = 5
b = 2
# k = int(input("Enter No :"))
# print(k)
try:
  print("open")
  c = a / b
  print(c)
  k = int(input("Enter No :"))
  print(k)

except ZeroDivisionError as e:
  print("Exception :", e)

except ValueError as e:
  print("Exception :", e)

except Exception as e:
  print("Exception :", e)
  # print("close")
  
finally:
  print("close")
print("Bye")

