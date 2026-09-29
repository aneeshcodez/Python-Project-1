def add(a,b) :
    return a + b

result = add(10,20)
print(result)

def test():
    print("A")
    return 10
    print("B") # This print statement does not get executed
    # because When Control reaches return, the function immediately stops and does not execute anything further


