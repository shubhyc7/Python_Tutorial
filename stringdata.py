#data type, data structures, sequence prg
datastring = 'ssss'
print(type(datastring))

txt = "Hello my friends"

x = txt.upper()

x = txt.swapcase()
x = txt.split()

x = txt.rindex("my")
x = txt.rfind("my")
print(x)


txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)


x = txt.lower()

print(x)


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)


txt = "THIS IS NOW!"

x = txt.isupper()

print(x)


txt = "   "

x = txt.isspace()

print(x)


txt = "565543"

x = txt.isnumeric()

print(x)


txt = "hello world!"

x = txt.islower()

print(x)


txt = "\u0033"  # unicode for 3

x = txt.isdecimal()

print(x)


txt = "Company123"

x = txt.isascii()

print(x)


txt = "CompanyX"

x = txt.isalpha()

print(x)


txt = "Company12"

x = txt.isalnum()

print(x)


txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)


txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
x = txt.endswith(".")

print(x)
x = txt.count("welcome")

print(x)

txt = "banana"

x = txt.center(20)

print(x)

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)


txt = "hello, and welcome to my world."

x = txt.capitalize()

print(x)
