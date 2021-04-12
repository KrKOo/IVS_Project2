from random import *
import os

if not os.path.exists("input"):
    os.mkdir("input")

# generate random coefficient from 1 to 10 (both included)
k = randint(1, 10)

# Generate 10 inputs
file = open("input/inputs10.txt", "w")

number = 0

for x in range(10):
    file.write(str(number) + "\n")
    number += k

file.close()

# Generate 100 inputs
file = open("input/inputs100.txt", "w")

number = 0

for x in range(100):
    file.write(str(number) + "\n")
    number += k

file.close()

# Generate 1000 inputs
file = open("input/inputs1000.txt", "w")

number = 0

for x in range(1000):
    file.write(str(number) + "\n")
    number += k

file.close()
