#
#   purpose: determine whether a number is prime or not, can be applied to ranges of numbers as well
#   author: zachary morrison
#   date written: 10/19/2020
#   Version: 1.0.0
#

#   imports
import math

#   background
print("The program below will test a range of numbers to find the primes!")
print("============================================================================\n\n")

#   functions/processing

#   primes_in_range tests a range of numbers to find the primes within the given range
#   return: primes in the given range


def primes_in_range(start, finish):
    primes = []
    for x in range(start, finish + 1):
        if is_prime(x):
            primes.append(x)

    print("\nThe prime numbers in the range of " + str(start) +
          " to " + str(finish) + " are: " + str(primes))
    return primes


#   is_prime tests if a number is prime
#   return: true or false based on if the number is prime


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False
    if num < 9:
        return True
    if num % 3 == 0:
        return False

    approx_sqrt = int(math.sqrt(num))

    for x in range(5, approx_sqrt + 1, 6):
        if num % x == 0 or num % (x + 2) == 0:
            return False
    return True


#   input
begin = int(input("Enter where you would like the program to begin: "))
end = int(input("Enter where you would like the program to end: "))

#   output
primes_in_range(begin, end)
