def outer():
    name = "Ram"

    def inner():
        print("Hello", name)

    return inner

# outer() # This returns nothing so we need to call inner (closure in this program),this is another justification
result = outer()
print(type(result))
result()


# How can I make myself understand this instead of you explain this to me,tell the best and easiest way to understand this myself