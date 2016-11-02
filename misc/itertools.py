i = itertools.combinations("ABCDEFG", 3)
for val in i:
    print(val)
##('A', 'B', 'C')
##('A', 'B', 'D')
##('A', 'B', 'E')
##('A', 'B', 'F')
##('A', 'B', 'G')
##('A', 'C', 'D')
##...

i = itertools.combinations_with_replacement("ABCDEFG", 3)
for val in i:
    print(val)	
##('A', 'A', 'A')
##('A', 'A', 'B')
##('A', 'A', 'C')
##('A', 'A', 'D')
##...

i = itertools.permutations("ABCDEFG", 3)
for val in i:
    print(val)
##('A', 'B', 'C')
##('A', 'B', 'D')
##('A', 'B', 'E')
##('A', 'B', 'F')
##...
    
i = itertools.count(10, 2)
for val in i:
    print(val)

##10
##12
##14
##16
##18
##20
##...
    
i = itertools.cycle("ABCD")
for val in i:
    print(val)

##A
##B
##C
##D
##A
##B
##...

i = itertools.repeat(10, 3)
for val in i:
    print(val)

##10
##10
##10
##...
