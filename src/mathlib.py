##
# @file mathlib.py
# @brief Implementation of the mathematical library.
# @author Kristián Kováč xkovac61
# Date: 28.3.2021


##
# @brief Addition of two numbers.
# @param x Number 1.
# @param y Number 2.
# @return The sum of the two numbers.

def add(x, y):
    return x + y 

##
# @brief Substraction of two numbers.
# @param x Number 1.
# @param y Number 2.
# @return The difference between the two numbers.

def sub(x, y):
    return x - y

##
# @brief Division of two numbers.
# @param x Divident.
# @param y Divisor.
# @return The quotient of the two numbers.
# @exception ZeroDivisionError When y equals to zero.

def div(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        raise e

##
# @brief Multiplication of two numbers.
# @param x Number 1.
# @param y Number 2.
# @return The Product of the two numbers.

def mul(x, y):
    return x * y

##
# @brief Factorial of a number.
# @param x Number to calculate the factorial of.
# @return The factorial of x.
# @exception ValueError When x is not a positive integer.

def fact(x):
    if(isinstance(x, float) and not x.is_integer()):
        raise ValueError("{} is not an integer.".format(x))
    if(x < 0):
        raise ValueError("{} is not a positive number.".format(x))
    res = 1
    for i in range(1, int(x) + 1):
        res = res * i
    return res

##
# @brief Power of a number.
# @param x Number to calculate the power of.
# @param y Exponent.
# @return The number x raised to the power of y.
# @exception ValueError When x is not a positive integer.

def pow(x, y):
    if(isinstance(y, float) and not y.is_integer()):
        raise ValueError("{} is not an integer.".format(x))
    if(y < 0):
        raise ValueError("{} is not a positive number.".format(x))

    return x ** y

##
# @brief Nth root of a number.
# @param x Number to calculate the root of.
# @param n Exponent.
# @return The n-th root of the number x.
# @exception ValueError When the exponent is less or equal to 0.
#   When the result would be a complex number.

def nth_root(x, n):
    if(n <= 0):
        raise ValueError("The exponent must be greater than 0.")
    if(x < 0):
        if(n % 2 == 0):
            raise ValueError("Coplex results not supported");
    
    res = x ** (1/n)

    return round(res, 10) 

##
# @brief Modulo of two numbers.
# @param x Divident.
# @param y Divisor.
# @return The remainder after division of x by y.
# @exception ValueError When the divisor is 0.

def mod(x, y):
    try:
        return x % y
    except ZeroDivisionError as e:
        raise e
