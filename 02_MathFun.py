# Min() and Max()

a = min(10,20,30)
b = max(10,20,30)
print(a)
print(b)

# abs()-> Return positive value

x = abs(-5.2)
print(x)

# pow(x,y) -> retrn x to the power of y

a = pow(2,3)
print(a)

'''
The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.
To use it, you must import the math module
'''

import math

x = math.sqrt(81)
print(x)

# math.ceil() -> round a number upward
# math.floor() -> round a number downword

x = math.ceil(1.4)
y = math.floor(1.4)

print(x,y)

y = math.pi

print(y)

# copysign(x, y) -> Returns x with the sign of y

print(math.copysign(4,-5))

# factorial(x)

y = math.factorial(5)
print(y)

# fmod(x, y) -> Returns the remainder when x is divided by y

x = math.fmod(5,3)
print(x)