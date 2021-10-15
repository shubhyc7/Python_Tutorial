def fib(n):
  
  a = 0
  b = 1

  if n ==1:
    print(b)
  
  
  else:
    print(a)
    print(b)
    for i in range(n):
      c = a+b
      print(c)
      a=b
      b=c


fib (4) 
