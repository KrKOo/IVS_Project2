from mathlib import *
from fileinput import *

# array numbers contains all numbers from stdin
numbers = []

# integer N is count of all numbers
N = 0

# load all numbers seperated with whitespace
# into numbers[] array and count numbers (N)
for line in input():
    for number in line.split():
        numbers.append(float(number))
        N = add(N, 1)

# float xs is sum of all given numbers
xs = 0.0

# float xsp is sum of all given numbers squared
xsp = 0.0

# calc the sum of all numbers - xs
# calc the sum of all numbers squared - xsp
for number in numbers:
    xs = add(xs, number)
    xsp = add(xsp, pow(number, 2))

# float result is the result
s = nth_root(( mul(div(1, sub(N, 1)), sub(xsp, mul(N, pow( mul(div(1,N), xs), 2)))) ), 2)

print(s)
