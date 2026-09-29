#*args
def kids_names(*kids) :
    print("The youngest kid is :" , kids[2])

kids_names("Ram","Sam","VK","BK")

#**kwargs
def kids_last_name(**kid_lname) :
    print("The last name of the kid :" , kid_lname["last_name"])

kids_last_name(first_name="Ram", last_name="Sam")

# RULE : While calling the function using parameters ,
# give the parameters like how you would normally give it for Postional / Keyword argument


