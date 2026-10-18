try:
    age = int(input("Enter your age: "))
    print(100/age)

except ZeroDivisionError:
    print("You cannot divide by zero")

except ValueError:
    print("Please enter a valid number")

else:
    print("Success!")

finally:
    print("Program Over")







'''
1.If you only write Try Block , you will get this error : SyntaxError: expected 'except' or 'finally' block
2.In the above program If they enter abc or 0, the except block executes, and else is skipped
3.'finally block' will always be executed no matter if an exception occurs or not.
'''

