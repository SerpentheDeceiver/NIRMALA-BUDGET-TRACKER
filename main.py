from BudgetTracker import BudgetTracker
from logo import logo, menu, greeter_text

RUNNING = True

# WELCOME
print(logo)
print(greeter_text.center(70))

# OBJECT INITIALIZATION
tracker = BudgetTracker()

while RUNNING:
    print(f"\n{menu}")
    try:
        choice = int(input('Enter Your Choice: '))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    # 1. Add Income
    if choice == 1:
        tracker.income()
    # 2. Add Expense
    elif choice == 2:
        tracker.expense()
    # 3. View All Transactions
    elif choice == 3:
        tracker.showalltransaction()
    # 4. View Balance
    elif choice == 4:
        tracker.viewbalance()
    # 5. Search Transactions
    elif choice == 5:
        tracker.searchtransaction()
    # 6. Save Data
    elif choice == 6:
        tracker.savedata()
    # 7. Load Data
    elif choice == 7:
        tracker.loaddata()
    # 8. Exit
    elif choice == 8:
        print("👋 BYE BYE!!")
        break
    else:
        print("❗ INVALID CHOICE!")
