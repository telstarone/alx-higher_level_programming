# ---------- ADVANCED FUNCTIONS ----------

# ---------- FUNCTIONS AS OBJECTS ----------
 
def mult_by_2(num):
    return num * 2
 
# A function can be
# 1. Assigned to another name
 
times_two = mult_by_2
 
print("4 * 2 =", times_two(4))
 
# 2. Passed into other functions
 
def do_math(func, num):
 
    return func(num)
 
print("8 * 2 =", do_math(mult_by_2, 8))
 
# 3. Returned from a function
 
def get_func_mult_by_num(num):
 
    # Create a dynamic function that will receive a value
    # and then return that value times the value passed
    # into getFuncMultByNum()
    def mult_by(value):
        return num * value
 
    return mult_by
 
generated_func = get_func_mult_by_num(5)
 
print("5 * 10 =", generated_func(10))
 
# 4. Embedded in a data structure
 
listOfFuncs = [times_two, generated_func]
 
print("5 * 9 =", listOfFuncs[1](9))
 
# ---------- PROBLEM ----------
# Create a function that receives a list and a function
# The function passed will return True or False if a list
# value is odd.
# The surrounding function will return a list of odd
# numbers
 
def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
 
def change_list(list, func):
 
    oddList = []
 
    for i in list:
        if func(i):
            oddList.append(i)
 
    return oddList
 
aList = range(1, 21)
 
print(change_list(aList, is_it_odd))
 
 
# ---------- FUNCTION ANNOTATIONS ----------
# It is possible to define the data types of attributes
# and the returned value with annotations, but they have
# no impact on how the function operates, but instead
# are for documentation
 
def random_func(name: str, age: int, weight: float) -> str:
    print("Name :", name)
    print("Age :", age)
    print("Weight :", weight)
 
    return "{} is {} years old and weighs {}".format(name, age, weight)
 
print(random_func("Derek", 41, 165.5))
 
# You don't get an error if you pass bad data
print(random_func(89, "Derek", "Turtle"))
 
# You can print the annotations
print(random_func.__annotations__)
 
# ---------- ANONYMOUS FUNCTIONS : LAMBDA ----------
# lambda is like def, but rather then assign the function
# to a name it just returns it. Because there is no name
# that is why they are called anonymous functions. You
# can however assign a lambda function to a name.
 
# This is their format
# lambda arg1, arg2,... : expression using the args
 
# lambdas are used when you need a small function, but
# don't want to junk up your code with temporary
# function names that may cause conflicts
 
# Add values
sum = lambda x, y : x + y
 
print("Sum :", sum(4, 5))
 
# Use a ternary operator to see if someone can vote
can_vote = lambda age: True if age >= 18 else False
 
print("Can Vote :", can_vote(16))
 
# Create a list of functions
powerList = [lambda x: x ** 2,
             lambda x: x ** 3,
             lambda x: x ** 4]
 
# Run each function on a value
for func in powerList:
    print(func(4))
 
 
# You can also store lambdas in dictionaires
 
attack = {'quick': (lambda: print("Quick Attack")),
           'power': (lambda: print("Power Attack")),
           'miss': (lambda: print("The Attack Missed"))}
 
attack['quick']()
 
# You could get a random dictionary as well for say our
# previous warrior objects
import random
 
# keys() returns an iterable so we convert it into a list
# choice() picks a random value from that list
attackKey = random.choice(list(attack.keys()))
 
attack[attackKey]()
 
# ---------- PROBLEM ----------
# Create a random list filled with the characters H and T
# for heads and tails. Output the number of Hs and Ts
# Example Output
# Heads :  46
# Tails :  54
 
# Create the list
flipList = []
 
# Populate the list with 100 Hs and Ts
# Trick : random.choice() returns a random value from the list
for i in range(1, 101):
    flipList += random.choice(['H', 'T'])
 
# Output results
print("Heads : ", flipList.count('H'))
print("Tails : ", flipList.count('T'))
 
 
# ---------- MAP ----------
# Map allows us to execute a function on each item in a list
 
# Generate a list from 1 to 10
oneTo10 = range(1, 11)
 
# The function to pass into map
def dbl_num(num):
    return num * 2
 
# Pass in the function and the list to generate a new list
print(list(map(dbl_num, oneTo10)))
 
# You could do the same thing with a lambda
print(list(map((lambda x: x * 3), oneTo10)))
 
# You can perform calculations against multiple lists
aList = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))
print(aList)
 
# ---------- FILTER ----------
# Filter selects items from a list based on a function
 
# Print out the even values from a list
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))
 
# ---------- PROBLEM ----------
# Find the multiples of 9 from a random 100 value list with
# values between 1 and 1000
 
# Generate a random list with randint between 1 and 1000
# Use range to generate 100 values
randList = list(random.randint(1, 1001) for i in range(100))
 
# Use modulus to find multiples of 9 by passing the random
# list to filter
print(list(filter((lambda x: x % 9 == 0), randList)))
 
 
# ---------- REDUCE ----------
# Reduce receives a list and returns a single result
 
# You must import reduce
from functools import reduce
 
# Add up the values in a list
print(reduce((lambda x, y: x + y), range(1, 6)))
