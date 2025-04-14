from TRANSACTION import Transaction

class BudgetTracker:

    def __init__(self):
        self.t = Transaction()

    def income(self):
        id_ = input("ID = ")
        date = input("DATE('YYYY-MM-DD') = ")
        amount = int(input("AMOUNT(₹) = "))
        category = input("CATEGORY = ")
        self.t.add(id_ = id_,date= date,type_="Income",amount=amount,category=category)

    def expense(self):
        id_ = input("ID = ")
        date = input("DATE('YYYY-MM-DD') = ")
        amount = int(input("AMOUNT(₹) = "))
        category = input("CATEGORY = ")
        self.t.add(id_=id_, date=date, type_="Expense", amount=amount, category=category)

    def showalltransaction(self):
        self.t.showalltransactions()

    def viewbalance(self):
        self.t.viewbalance()

    def searchtransaction(self):
        self.t.searchtransaction()

    def savedata(self):
        self.t.savedata()

    def loaddata(self):
        self.t.loaddata()