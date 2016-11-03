#INDEXING
    >>> "Binary Bears"[:3]
    'Bin'
    >>> "Binary Bears"[3:]
    'ary Bears'
    >>> "Binary Bears"[3:4]
    'a'
    >>> "Binary Bears"[::2]
    'Bnr er'
    >>> "Binary Bears"[::-1]
    'sraeB yraniB'

#LIST COMPREHENSIONS
    >>> l = [1, 2, 3, 4]
    >>> [num+1 for num in l]
    [2, 3, 4, 5]
    >>> ["Case " + str(num) for num in l]
    ['Case 1', 'Case 2', 'Case 3', 'Case 4']

#CHANGE CASE
    "BINARY BEARS".lower() 		-> 'binary bears'
    "binary bears".upper() 		-> 'BINARY BEARS'
    "binary BEARS".swapcase()	-> 'BINARY bears'

    #Other Change Case
    "binary bears".capitalize()	-> 'Binary bears'
    "binary bears".title()		-> 'Binary Bears'

    #Case Conditionals
    "binary bears".isupper()    -> False
    "binary bears".islower()    -> True
    "binary bears".istitle()    -> False

#FIND AND COUNT
    #Find
    "binary bears".find('a') = 3
    "binary bears".rfind('a') = 9 #Return the highest index
    "binary bears".index('bear') = 7 #Like find(), but raise ValueError when the substring is not found.
    "binary bears".rindex('a') = 9

    #In
    "bear" in "binary bears" = True

    #Count
    "binary bears".count('bear') = 1

#Conditionals
    str.isalpha()       
    str.isnumeric() 
    str.isdecimal() 
    str.isdigit()
    str.isalnum()
    str.isspace()    #" ","\t","\n","\r","\f"

#Split
    >>> "Red fish, Blue Fish, Green Fish".split(',')    
    ['Red fish', ' Blue Fish', ' Green Fish']

    >>> "Red fish, Blue Fish, Green Fish".split(',', maxsplit=1)    
    ['Red fish', ' Blue Fish, Green Fish']

    >>> "Line1\nLine2\nLine3\n".splitlines()
    ['Line1', 'Line2', 'Line3']

    >>> "Line1\nLine2\nLine3\n".splitlines(keepends=True)
    ['Line1\n', 'Line2\n', 'Line3\n']

#Strippers
    "     B e a r   ".strip()  = 'B e a r'
    "     Bear   ".lstrip()     = 'Bear   '
    "     Bear   ".rstrip()    = '     Bear'

#Format
    >>> "1".zfill(2)
    '01'
    >>> "123".rjust(6)
    '   123'
    >>> "123".ljust(6)
    '123   '
    >>> "123".center(6)
    ' 123  '                      
    >>> "{0:.1f}".format(123.15)
    '123.2'

#Constants
    import string
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string.ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    string.ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    string.digits = "0123456789"
    string.hexdigits = "0123456789abcdefABCDEF"
    string.octdigits = "01234567"

    string.punctuation = '!"#$%&''()*+,-./:;<=>?@[\]^_`{|}~'
    string.printable
    string.whitespace
