import pandas as pd
from logo import searchmenu
from CsvFileHandler import CSVHandler

class Transaction:

    def __init__(self):
        self.csv = CSVHandler()
        self.record = []

    def add(self,id_,date,type_,amount,category):
        item = {"id":id_,"date":date,"type":type_,"amount":amount,"category":category}
        self.record.append(item)

    def viewbalance(self):
        amount = 0
        for i in self.record:
            if i['type'].lower() == 'expense':
                amount -= i['amount']
            elif i['type'].lower() == 'income':
                amount += i['amount']
        print(f"\nCURRENT AVAILABLE BALANCE --> ₹{amount}", end='')
        if amount < 0: print(" <(-)ve ₹Amount Indicates Credit(loan)>")

    def showalltransactions(self) -> None:
        print("\n<-- RECORD'S -->")
        print(f"{pd.DataFrame(self.record)}")

    def searchtransaction(self):
        print(searchmenu)
        choice = int(input("ENTER YOUR CHOICE:"))
        #INVALID
        if choice>5 or choice<1: print("INVALID CHOICE!")
        match_transaction = []
        #1
        if choice == 1:
            searchdate = input("ENTER DATE TO SEARCH ('YYYY-MM-D'):")
            for item in self.record:
                if item['date'] == searchdate:
                    match_transaction.append(item)
        #2
        if choice == 2:
            type_ = input("ENTER TYPE TO SEARCH ('Income/Expense'):")
            for item in self.record:
                if item['type'].lower() == type_.lower():
                    match_transaction.append(item)
        #3
        if choice == 3:
            category = input("ENTER CATEGORY TO SEARCH :")
            for item in self.record:
                if item['category'].lower() == category.lower():
                    match_transaction.append(item)
        #4
        if choice == 4:
            rangefrom = int(input("ENTER AMOUNT RANGE FROM : "))
            rangeto = int(input("RANGE TO :"))
            for item in self.record:
                if rangefrom <= item['amount']<=rangeto:
                    match_transaction.append(item)
        #5
        if choice == 5:
            id_ = int(input("ENTER ID TO SEARCH : "))
            for item in self.record:
                if str(item['id']) == str(id_):
                    match_transaction.append(item)

        if match_transaction == []: print("\nNO MATCHED TRANSACTION'S !")
        else:
            print("\n<--MATCHED RECORD'S-->")
            print(f"{pd.DataFrame(match_transaction)}")

    def savedata(self) -> None:
        #SORT BY DATE USING FUNCTION (key)
        self.record = sorted(self.record, key= lambda x: x['date'])
        self.csv.save(self.record)

    def loaddata(self) -> None:
        self.record = self.csv.load()
