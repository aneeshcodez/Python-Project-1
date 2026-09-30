# Title : Personal Expense Analyzer

# Expenses

expense_1 = {
    "Item": "Shoe",
    "Category": "Personal",
    "Amount": 1000
}

expense_2 = {
    "Item": "Pizza",
    "Category": "Food",
    "Amount": 200
}

expense_3 = {
    "Item": "Burger",
    "Category": "Food",
    "Amount": 500
}

expense_4 = {
    "Item": "Watch",
    "Category": "Personal",
    "Amount": 2000
}

# Declaring it globally
expenses_list = [expense_1, expense_2, expense_3, expense_4]


# View all expenses

def view_expenses():
    for expense in expenses_list :
        print(expense["Item"],expense["Category"],expense["Amount"] ) # Learned this



# Calculate total money spent

def calc_total_amount():
    total_amount = 0
    for expense in expenses_list:
        total_amount = total_amount + expense["Amount"]
    print(total_amount)


# Show unique expense categories

def unique_categories():
    set_unique = set()
    for expense in expenses_list:
        set_unique.add(expense["Category"])
    print(set_unique)


# Calculate spending for a particular category

def calc_amount_particular_category(cate):
    particular_amount = 0
    for expense in expenses_list:
        if (expense["Category"] == cate):
            particular_amount = particular_amount + expense["Amount"]
    print(particular_amount)


# Segregating all the Amounts of expenses into a list for further operations. This list would be global

amounts_list = []
for expense in expenses_list:
    amounts_list.append(expense["Amount"])



# Find the biggest expense

def find_biggest_expense():
    big = amounts_list[0]
    for amounts in amounts_list:
        if amounts > big:
            big = amounts
    print(big)


# Show the total number of expenses

def calc_total_no_expenses():
    total_no = len(amounts_list)
    print(total_no)

# Final Summary

def final_summary():
    total_expenses = len(expenses_list)
    total_money_spent = 0
    categories = set()

    for expense in expenses_list:
        total_money_spent = total_money_spent + expense["Amount"]
        categories.add(expense["Category"])

    print("Total No of Expenses :" , total_expenses)
    print("Total Money Spent :" , total_money_spent)
    print("Total Categories :" , categories)

# Calling all the functions
view_expenses()
calc_total_amount()
unique_categories()
calc_amount_particular_category("Food")
calc_amount_particular_category("Personal")
find_biggest_expense()
calc_total_no_expenses()
final_summary()

# Correction 1 :
'''
find_biggest_expense() without amounts_list

You can directly work with expenses_list:
code :

def find_biggest_expense():
    big = expenses_list[0]["Amount"]

    for expense in expenses_list:
        if expense["Amount"] > big:
            big = expense["Amount"]

    print(big)
'''



