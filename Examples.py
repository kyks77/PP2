
#Examples

#1
print("Hello, World!")

#2
if 5 > 2:
  print("Five is greater than two!")

#3
if 5 > 2:
 print("Five is greater than two!")  
if 5 > 2:
        print("Five is greater than two!") 

#4
#This is a comment.
print("Hello, World!")

#4.1
#print("Hello, World!")
print("Cheers, Mate!")

#4.2
print("Hello, World!") #This is a comment.
#4.3
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!") 

#5,01
x = 5
y = "John"
print(x)
print(y)

#5,02
x = 4
x = "Sally"
print(x)

#5,03
x = str(3)
y = int(3)
z = float(3)

print(x)

#5,04
a = 4
A = "Sally"

print(a)
print(A)

#5,11

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#5,21
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#5,22
x = y = z = "Orange"

print(x)
print(y)
print(z)

#5,31
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#5,32
x = 5
y = 10
print(x + y)

#5,33
x = 5
y = "John"
print(x + y)
#Outputs an error

#5,34
x = 5
y = "John"
print(x, y)
#Supports different data types 

#5,41
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#5,42
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#5,43
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#5,44
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#6
x = 5
print(type(x)) 

#7,1
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#7,2
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#7,3
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#7,4
import random

print(random.randrange(1, 10))

#7,5
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)a

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#8,11
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#8,12
a = "Hello"
print(a)

#8,13
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

 # Or you can do the following
 
 a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#8,14
a = "Hello, World!"
print(a[1])

#8,15
for x in "banana":
  print(x) 

#8,16
a = "Hello, World!"
print(len(a))

#8,17
txt = "The best things in life are free!"
print("free" in txt)

#8,18
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#8,19
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#8,21
b = "Hello, World!"
print(b[2:5])

#8,22
b = "Hello, World!"
print(b[:5])

#8,23
b = "Hello, World!"
print(b[2:])

#8,24
b = "Hello, World!"
print(b[-5:-2])

#8,31
a = "Hello, World!"
print(a.upper())

#8,32
a = "Hello, World!"
print(a.lower())

#8,33
a = " Hello, World! "
print(a.strip())

#8,34
a = "Hello, World!"
print(a.replace("H", "J"))

#8,35
a = "Hello, World!"
b = a.split(",")
print(b)

#8,41
a = "Hello"
b = "World"
c = a + b
print(c)

#8,42
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#8,51
age = 36
txt = "My name is John, I am " + age
print(txt) 
#Outputs an error
#8,52
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#8,53
price = 59
txt = f"The price is {price} dollars"
print(txt)

#8,54
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#8,55
txt = f"The price is {20 * 59} dollars"
print(txt)

#8,61
txt = "We are the so-called "Vikings" from the north."


#You will get an error if you use double quotes inside a string that are surrounded by double quotes:

#8,62
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
