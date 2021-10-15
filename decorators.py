# def div(a,b):
#   if(a < b):
#     a,b = b,a 
#   return a/b

# print(div(4,2))
# print(div(2,4))


def div(a, b):
  return a/b


def smart_div(func):
  def inner(a,b):
    if(a < b):
      a, b = b, a
    return func(a,b)

  return inner

div = smart_div(div)  
print(div(4, 2))
print(div(2, 4))
