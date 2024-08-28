name = 'The Rock'
wt_kg = 118
wt_lb = 259.6

#  f-string method (henceforth, SF1)
print(f'{name} weighs {wt_kg} kg or {wt_lb} lbs.')

# % - formatting method (henceforth, SF2)
print('%s weighs %d kg or %f lbs.'%(name, wt_kg, wt_lb))
print('%s weighs %d kg or %.1f lbs.' % (name, wt_kg, wt_lb))

# %d is for the real number not string
# print('%d weighs %d kg or %.1f lbs.' % (name, wt_kg, wt_lb))

# .format() method (henceforth, SF3)
print('{} weighs {} kg or {} lbs.'.format(name, wt_kg, wt_lb))

x = 5
print(f'{x} squared is {x ** 2}.')
print('%d squared is %d.' % (x, x ** 2))
print('{} squared is {}.'.format(x, x ** 2))
print('%s weighs %.1f kg or %d lbs.' % (name, wt_kg, wt_lb))

# For SF2, %s, %d, and %f are called conversion specifiers, and
# as the name implies, they can be used to convert variables.

print('%s weighs %s kg or %s lbs.' % (name, wt_kg, wt_lb))
print('%s weighs %.1f kg or %d lbs.' % (name, wt_kg, wt_lb))

print('Two to the power of 32 is {2 ** 32}.')

name = {'first': 'Joseph', 'last': 'Gordon-Levitt'}
print(f'{name['first']} {name['last']} is an American actor.')

print(f'{name['first'].upper()} {name['last'].upper()} is an American actor.')

names = ['Sam', 'Mohamed', 'Yang', 'Maria', 'Mani']
for name in names:
    print('Hello, {}!'.format(name))

pi = 3.141592653
print('Pi to two-decimal places is {:.2f}'.format(pi))

print(F'Pi to two-decimal places of accuracy is {pi:.2f}')



