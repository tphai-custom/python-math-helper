import math
print("Welcome to the Daily Expense Tracker!")
print()
print('''Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit''')
expense = []
total = "unset"
average = "unset"
while True:
    a1 = int(input())
    if a1 == 5:
        print('Exiting the Daily Expense Tracker. Goodbye!')
        break
    elif a1 == 1:
        a2 = float(input())
        expense.append(a2)
        print("Expense added successfully!")
    elif a1 == 2:
        if len(expense) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for index, phantu in enumerate(expense):
                print(f"{index + 1}. {phantu}")
    elif a1 == 3:
        if len(expense) == 0:
            print("No expenses recorded yet.")
        else:
            total = sum(expense)  
            average = total / len(expense)  
            print(f"Total expense: {total}")
            print(f"Average expense: {average}")
    elif a1 == 4:
        expense.clear()
        print("All expenses cleared.")
    else:
        print("Invalid choice. Please try again.")
		
	