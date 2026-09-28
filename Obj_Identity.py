a = [1,2,3]
b = [1,2,3]

print(a==b) # True
# The id() function in Python returns the memory address where of the object
print(id(a))
print(id(b))
print(a is b) # False because memory address of a and b are diff

# a = [1,2,3]
# b = a
# print(a is b ) # True
#
#
#
