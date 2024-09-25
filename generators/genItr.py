""" Exception - print(itr.next()) This works in Python 2 """
####################################################################################################################################
""" Iterator """

""" Taking an iterable """
item = "BEAUTIFUL"

""" Making the 'item' as an iterator and storing it in iterator object 'itr' """
itr = iter(item)

""" Using itr: iterator object """
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

""" Using for loop """
for x in iter(item):
    print(x)

####################################################################################################################################
""" Genarator """

""" Creating a generator function """
def give_item(limit):
    i = 1
    while i <= limit:
        """ using of keyword: yield """
        yield i
        i += 1

""" Using next repeatedly here, will give 1 each time cause the function is getting called each time """
print(next(give_item(10)))
print(next(give_item(10)))

""" Printing the values through generator function """
for x in give_item(10):
    print(x)

""" Creating a generator object and printing values through it """
values = give_item(10)

""" 
Commenting the loop below because:
The loop consumes all the items produced by the generator values. 
After this loop finishes, the generator is exhausted, meaning it has no more items to yield.
Hence, the below print statements couldn't be continued.
For all the iterations.

"""

# for x in values:
#     print(x)

""" Printing through the generator object 'values' """ 
print(next(values))
print(next(values))   
print(next(values))   
print(next(values))   
print(next(values))   
print(next(values))   
print(next(values))   
print(next(values))   
print(next(values))   
print(next(values))   

####################################################################################################################################
""" Generator Expressions """

def squarenum(x):
    return x*x

""" Creating a generator expression """
iteratorobj = (squarenum(x) for x in range(10,70,10))

""" Printing few of the values """
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(next(iteratorobj))
print(next(iteratorobj))

""" More short way """
square_generator = (n** 2 for n in range(1,6))

""" Printing the generator object and values. """
print(square_generator)

for x in square_generator:
    print(x)