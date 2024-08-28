import time
import cProfile

t1 = time.time()

def greetings(name):
    return f"Hello, {name}!!"

name = input("Give your name: ")
print(greetings(name))

t2 = time.time()
interval = round((t2 - t1), 2)

print("excecution time: ",interval, 's.')
print(cProfile.run('greetings(name)'))

# for i in range(30):
#     time.sleep(1)

