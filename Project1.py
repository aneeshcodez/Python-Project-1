# This project is to build something after learning Lists, Tuple, Sets & Dict

# 1. Add a Contact

user_1 = {
    "name" : "Ram",
    "Location" : "Chennai",
    "Age" : 25
}

user_2 = {
    "name" : "Sam",
    "Location" : "Salem",
    "Age" : 26
}

user_3 = {
    "name" : "Sammy",
    "Location" : "Salem",
    "Age" : 46
}

contact_list = [user_1, user_2]

# 2. View all contacts

for user in contact_list :
    print(user.values())

# 3. Search for a particular contact by name
# completely got it wrong
for user in contact_list :
    if user["name"] == "Ram" :
        print(user["name"])

# 4. Delete a contact

#contact_list.pop(0)

# 5. Show all unique cities your contacts are from

for user in contact_list :
    set_1 = set()
    set_1.add(user["Location"])
    print(set_1)

# 6. Show how many contacts you have

no = len(contact_list)
print(no)

