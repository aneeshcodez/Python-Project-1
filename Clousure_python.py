def outer():
    name = "Ram"

    def inner():
        print("Hello", name)

    return inner

# We are storing inner() function's object in result. it was returned by outer function
result = outer()
print(type(result)) # result is a function object
result()

'''
Reference Program : 

def greet():
    print("Hello")

another_function = greet
another_function() # instead of greet()

-------------------------------------------------------
A closure allows a function to remember information from its enclosing scope, even after the enclosing function has finished executing.We want an inner function to retain access to variables from its enclosing function even after the enclosing function has finished executing.

And one important clarification: closures don't keep the entire outer function running. The outer function finishes; Python retains the necessary referenced variable bindings for the inner function.

That's the fundamental idea behind closures.
'''

