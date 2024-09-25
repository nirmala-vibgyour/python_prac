""" General property of a function """

def func():
    return "Hello!"

""" A function reference stored in the variable"""
funcRef = func  
print(funcRef)  

""" Actual function value stored in a variable """
result = func()
print(result)  

####################################################################################################################################
""" Decorators """


""" Example: 1 """

""" Declaring a function to be used as a decorator """
def deco(func):
    def wrap():
        print("This is inside of wrapper/inner function.")
        
        """ Wherever, func() return value is printed so the remaining body of func() is executed before that. """
        print("This is printing the decorated function: \n", func())
        
        return "This is return of inner function", func()
    print("This is outer function line ")
    return wrap

@deco
def to_be_decorated():
    print("Hi, I am exicited!!")
    return "I am getting decorated "

""" Printing the decorated function as they are not callable at this case """
print(to_be_decorated())



""" Example: 2 """

def tempKelvin(func):
    
    """ As arguments: (*args, **kwargs) """
    def convertTemp(temp):
        tempCelcius = func(temp)
        kelvinTemp = tempCelcius + 273
        return kelvinTemp
    
    return convertTemp

@tempKelvin
def getCelcius(tempp):
    return tempp

print("Temp in Kelvin: ", getCelcius(20))



""" Example: 3 """

def cache(func):
    cached_results = {}

    def wrapper(*args):
        if args in cached_results:
            print("Returning cached result for:", args)
            return cached_results[args]
        else:
            print("Calculating result for:", args)
            result = func(*args)
            cached_results[args] = result
            return result

    return wrapper

@cache
def expensive_computation(x, y):
    # Simulate a time-consuming computation
    import time
    time.sleep(2)  # Sleep for 2 seconds
    return x + y

# Example usage
print(expensive_computation(1, 2))  # Calculating result
print(expensive_computation(1, 2))  # Returning cached result
print(expensive_computation(2, 3))  # Calculating result


""" Example: 4 """

def log_execution(level, message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}] {message}: Starting {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"[{level}] {message}: Finished {func.__name__}")
            return result
        return wrapper
    return decorator

@log_execution(level="INFO", message="Executing")
def add(a, b):
    return a + b

@log_execution(level="DEBUG", message="Running")
def multiply(a, b):
    return a * b

# Example usage
print(add(5, 3))        # Logs execution
print(multiply(4, 2))   # Logs execution




""" Example: 5 """

def enforce_types(*arg_types, **kwarg_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check positional arguments
            if len(args) != len(arg_types):
                raise TypeError(f"{func.__name__} expects {len(arg_types)} positional arguments, got {len(args)}")
            for arg, expected_type in zip(args, arg_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {arg} is not of type {expected_type.__name__}")

            # Check keyword arguments
            for key, expected_type in kwarg_types.items():
                if key in kwargs and not isinstance(kwargs[key], expected_type):
                    raise TypeError(f"Keyword argument '{key}' is not of type {expected_type.__name__}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@enforce_types(int, int)  # Expecting two integers
def add(a, b):
    return a + b

@enforce_types(float, int, multiplier=float)  # Expecting a float, an int, and a float for 'multiplier'
def multiply(a, b, multiplier=1.0):
    return a * b * multiplier

# Example usage
print(add(5, 3))            # Valid
print(multiply(4.0, 2))     # Valid
print(multiply(4.0, 2, multiplier=2.5))  # Valid

# Uncommenting the following lines will raise TypeErrors
# print(add(5, "3"))        # TypeError: Argument 3 is not of type int
# print(multiply(4.0, 2, multiplier="2.5"))  # TypeError: Keyword argument 'multiplier' is not of type float


