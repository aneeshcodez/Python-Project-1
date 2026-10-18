try:
    number = int("Hello")

except ValueError as error:
    print(error)
    print(type(error))
    print("Something went wrong ->",error)