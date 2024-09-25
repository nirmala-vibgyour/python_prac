import time

def foo():
    print("I am foo function body.")
    return (9+2)

resultFoo = foo()

""" To note that function body is executed when it is called and before the return value is collected."""
time.sleep(10)

print(resultFoo + 12)