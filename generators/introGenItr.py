names = ["java", "python", "c++", "c#", "javascript", "rust", "html", "css", "typescript"]

""" j is <list_iterator object at 0x0000018FAA6D1330> """
j = iter(names)
print(j)
""" This is the same iterator object j: <list_iterator object at 0x000002072AA41360> """
print(j.__iter__())

""" Printing the items in the iterator """
# print(j.__next__())
# print(j.__next__())
# print(j.__next__())
# print(j.__next__())
# print(j.__next__())
# print(j.__next__())
# print(j.__next__())
# print(j.__next__())
# print(j.__next__())
""" This next print(j.__next__()) will cause error. """
# print(j.__next__())


""" j.next() gives error. """
try:
    print(j.__next__())
    print(j.__next__())
    print(j.__next__())
    print(j.__next__())
    print(j.__next__())
    print(j.__next__())
    print(j.__next__())
    print(j.__next__())
    print(j.__next__())
    print(j.__next__())
    print(j.__next__())
except StopIteration:
    print("The list ends here.")

print("The list must be printed once.")

""" This prints nothing. 

for x in j.__iter__():
    print(x)
or

for x in j:
    print(x)

"""

""" This prints the same object as j, no new object is created. """
print(iter(j))

""" This prints the names."""
for x in iter(names):
    print(x)

""" This prints the the same list as above."""
for x in names:
    print(x)


""" This is the generator function. 'yield' keyword is mandatory. """
def name(items):
    i = 0
    while i > len(items):
        yield items[i]
        i += 1

""" f is the generator"""
f = name(names)
print(f)

""" This gives error StopIteration.

print(f.__next__())
or
print(next(f))

"""
