def add_expense(expenses,category,amount):
    expenses.append({'category':category,'amount':amount})
    
def total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)

def average_expense(expenses):
    if not expenses:
        return 0
    return total_expenses(expenses) / len(expenses)

# create a empty list
expenses=[]

add_expense(expenses, 'groceries', 100)
add_expense(expenses, 'rent', 500)
add_expense(expenses, 'entertainment', 300)

expenses_sorted = sorted(expenses,key = lambda x: x['amount'])
print("Expenses:")
for expense in expenses_sorted:
    print(f"Category:{expense['category']}, Amount: ₹{expense['amount']}")
total = total_expenses(expenses)
average = average_expense(expenses)

print(f"\nTotal Expenses: ₹{total}")
print(f"Average Expenses:.₹{average}")