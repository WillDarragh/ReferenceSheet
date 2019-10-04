# Python Tricks

# For - Else Loop
for x in range(10):
    if x%2 == 0:
        print('Even found :)')
        break
else: # Only runs if never broke out of loop
    print('No evens found :(')

# Swapping numbers in place
x, y = 10, 5
x, y = y, x

# Join List into String
string = ''.join(['These ', 'are ', 'some ','strings.'])

# Chaining Comparison Operators
n = 10
print( 20 > n < 1 )
print( 1 < n < 20 )

# Enums in Python
class person:
    name, age = range(2)
print(person.name)
print(person.age)

# Most frequent value in list
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4] 
print(max(set(test), key = test.count)) 

# Multiplying strings
print('string'*5)

# Check for anagrams
from collections import Counter 
def is_anagram(str1, str2): 
     return Counter(str1) == Counter(str2) 
print(is_anagram('geek', 'eegk')) 
  
print(is_anagram('geek', 'peek')) 

# Lambda Functions
weird_list = [('a',10),('b',15),('c',-15)]
print(sorted(weird_list, key = lambda x: x[1]))

# Print Unpacked List
words = ['These','are','words']
print(*words, sep=' ')

# Map Input
the_input = '1 2 3 4'
a, b, c, d = map(int, the_input.split())

# Extended Unpacking
the_input = '1 2 abc def ghi 20'
x, y, *words, mult = the_input.split() 
