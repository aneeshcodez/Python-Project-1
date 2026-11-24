try:
    x = "hello"

    if not type(x) is int:
        raise TypeError("Only integers are allowed")

except TypeError as error:
    print(error)