import threading, time
print('Start of program.')

def takeNap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target = takeNap)  # not takeNap()

print('End of program.')

# create and start new thread and will execute the function in new thread of execution after the first one is completed.
threadObj.start()
# a program will not terminate until all its threads have terminated.
print(type(threadObj))

# getting printed in their own thread, means: started and ended here, a new thread.
threadObj1 = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj1.start()