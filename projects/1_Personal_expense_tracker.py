# A simple program where the user enters expenses,
# and the script stores and summarizes them.

expenses=[]
def add_expense():
    amount=float(input("enter amount:"))
    category=input("enter category:")
    description=input("enter description:")

    expense={
        "amount":amount,
        "category":category,
        "description":description
    }

    expenses.append(expense)
    print("Expense added successfully!")
def show_summary():

    
    if not expenses:
        print("No expenses recorded.")
        return
    total=sum(exp['amount'] for exp in expenses)
    print("********Expense Summary********")
    print(f"Total expenses: ${total}")
    category_map={}
    for exp in expenses:
        cat=exp["category"]
        category_map[cat]=category_map.get(cat,0)+exp["amount"]

    print("expensed by category:")
    for cat, amount in category_map.items():
        print(f"  {cat}: ${amount}")

    print(f"(total entries: {len(expenses)}")


while True:
    print("1.add ")
    print("2.summary")
    print("3.exit")

    choice=input("choose an option:")

    if choice=="1":
        add_expense()
    elif choice=="2":
        show_summary()
    elif choice=="3":
        print("exiting...")
        break
    else:
            print("invalid choice, try again.")