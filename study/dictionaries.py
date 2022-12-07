##Dictionaries##

"""It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary). 
A pair of braces creates an empty dictionary: {}. 
Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; 
this is also the way dictionaries are written on output.

The main operations on a dictionary are storing a value with some key and extracting the value given the key. 
It is also possible to delete a key:value pair with del. 
If you store using a key that is already in use, the old value associated with that key is forgotten. 
It is an error to extract a value using a non-existent key.

Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, 
in insertion order (if you want it sorted, just use sorted(d) instead). 
To check whether a single key is in the dictionary, use the in keyword.

Here is a small example using a dictionary:"""

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
4098
del tel['sape']
tel['irv'] = 4127
tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
['jack', 'guido', 'irv']
sorted(tel)
['guido', 'irv', 'jack']
'guido' in tel
True
'jack' not in tel
False

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

{x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}

# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

gallahad the pure
robin the brave

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

0 tic
1 tac
2 toe

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

#To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

for i in reversed(range(1, 10, 2)):
    print(i)

9
7
5
3
1

# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

apple
apple
banana
orange
orange
pear

# Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

apple
banana
orange
pear

# It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
