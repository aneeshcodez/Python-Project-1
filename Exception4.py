try:
    number = int("Hello")

except Exception as error:
    print("Error message :",error)
    print("Error type :", type(error).__name__)
    # Re Raising
    raise



'''
Re-raise an exception:Sometimes you catch an exception to log it or perform some action, 
but you still want the calling code to know that the operation failed.
'''