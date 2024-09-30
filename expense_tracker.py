from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from collections import defaultdict
import sqlite3
def add():
    while True:
        mode = input('''Please enter the mode of transaction:
                     1. For cash -> Press 1
                     2. For bank -> Press 2
                     3. For both -> Press 3
                     4. To return back to main menu -> Press 4 ''')
        if mode.isdigit():
            if mode == '1':
                amount = input("Please enter the amount spent on transaction: ")
                category = input("Please enter the category of spending: ")
            

                if amount.isdigit():
                    amount =int(amount)
                    data = sqlite3.connect("Tracker.db")
                    cur = data.cursor()
                    cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":0-amount,"Bank":0,"Credit":0,"Debit":amount})
                    data.commit()
                    data.close()

                    data = sqlite3.connect("Tracker.db")
                    cur = data.cursor()
                    Day = datetime.now().day
                    Month = datetime.now().month
                    Year = datetime.now().year
                    amount = int(amount)
                    cur.execute("INSERT INTO Transaction_Record VALUES (:Day,:Month,:Year,:Amount,:Category)",{'Day':Day,'Month':Month,'Year':Year,'Amount':amount,'Category':category})
                    data.commit()
                    data.close()
                    print("Your transaction has been recorded.")
                else:
                    print("Invalid Operation! Please enter valid input...")
            elif mode == '2':
                amount = input("Please enter the amount spent on transaction: ")
                if amount.isdigit():
                    amount = int(amount)
                    category = input("Please enter the category of spending: ")
                    data = sqlite3.connect("Tracker.db")
                    cur = data.cursor()
                    cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":0,"Bank":0-amount,"Credit":0,"Debit":amount})
                    data.commit()
                    data.close()

                    data = sqlite3.connect("Tracker.db")
                    cur = data.cursor()
                    Day = datetime.now().day
                    Month = datetime.now().month
                    Year = datetime.now().year
                    amount = int(amount)
                    cur.execute("INSERT INTO Transaction_Record VALUES (:Day,:Month,:Year,:Amount,:Category)",{'Day':Day,'Month':Month,'Year':Year,'Amount':amount,'Category':category})
                    data.commit()
                    data.close()
                    print("Your transaction has been recorded.")
                else:
                    print("Invalid Operation! Please enter valid input...")
            elif mode == '3':
                debit_cash = input("Please enter the amount to be debited in cash: ")
                debit_bank = input("Please enter the amount to be debited in bank: ")
                        
                if debit_cash.isdigit() and debit_bank.isdigit():
                    debit_cash = int(debit_cash)
                    debit_bank = int(debit_bank)
                    category = input("Please enter the category of spending: ")
                    data = sqlite3.connect('Tracker.db')
                    cur = data.cursor()
                    cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":0-debit_cash,"Bank":0-debit_bank,"Credit":0,"Debit":debit_cash+debit_bank})
                    data.commit()
                    data.close()

                    data = sqlite3.connect("Tracker.db")
                    cur = data.cursor()
                    Day = datetime.now().day
                    Month = datetime.now().month
                    Year = datetime.now().year
                    cur.execute("INSERT INTO Transaction_Record VALUES (:Day,:Month,:Year,:Amount,:Category)",{'Day':Day,'Month':Month,'Year':Year,'Amount':debit_bank+debit_cash,'Category':category})
                    data.commit()
                    data.close()
                    print("Your transaction has been recorded.")
                else:
                    print("Invalid Operation! Please enter valid input...")
            elif mode == '4':
                break  
            else:
                print("Invalid Operation! Please enter valid input...")
                     
        else: 
            print("Invalid Operation! Please enter valid input...")

def remove():
    while True:
        Day = input("Enter the day of the record to be removed: ")
        Month = input("Enter the month of the record to be removed: ")
        Year = input("Enter the year of the record to be removed: ")
        if Day.isdigit() and Month.isdigit() and Year.isdigit():
            mode = input('''Enter the mode of transaction: 
                            1. For cash -> Press 1
                            2. For bank -> Press 2
                            3. For both -> Press 3
                            4. To exit to previous menu -> Press 4 ''')
            if mode.isdigit():
                if int(Day)>31 and int(Month)>12 and int(Year)>2050 and int(Year)<2000 and int(Day)<1 and int(Month)<1:
                        print("Invalid Operation! Please enter valid input...")
                else:
                    
                    if mode == '1':
                        amount = input("Enter the amount of transaction: ")
                        if amount.isdigit():
                            data = sqlite3.connect("Tracker.db")
                            cur = data.cursor()
                            cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":int(amount),"Bank":0,"Credit":int(amount),"Debit":0})
                            data.commit()
                            data.close()

                            data = sqlite3.connect("Tracker.db")
                            cur = data.cursor()
                            cur.execute("DELETE FROM Transaction_Record WHERE Day = :Day AND Month =:Month AND Year =:Year AND Amount = :Amount", {'Day':Day,'Month':Month,'Year':Year,'Amount':int(amount)})
                            data.commit()
                            data.close()
                            print("The transaction record has been deleted.")
                        else:
                            print("Invalid Operation! Please enter valid input...")

                    elif mode == '2':
                        amount = input("Enter the amount of transaction: ")
                        if amount.isdigit():
                            data = sqlite3.connect("Tracker.db")
                            cur = data.cursor()
                            cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":0,"Bank":int(amount),"Credit":int(amount),"Debit":0})
                            data.commit()
                            data.close()

                            data = sqlite3.connect("Tracker.db")
                            cur = data.cursor()
                            cur.execute("DELETE FROM Transaction_Record WHERE Day = :Day AND Month =:Month AND Year =:Year AND Amount = :Amount", {'Day':Day,'Month':Month,'Year':Year,'Amount':int(amount)})
                            data.commit()
                            data.close()
                            print("The transaction record has been deleted.")
                        else:
                            print("Invalid Operation! Please enter valid input...")
                    elif mode == '3':
                        credit_cash = input("Please enter the amount to be credited in cash: ")
                        credit_bank = input("Please enter the amount to be credited in bank: ")
                                
                        if credit_cash.isdigit() and credit_bank.isdigit():
                            credit_cash = int(credit_cash)
                            credit_bank = int(credit_bank)
                            data = sqlite3.connect('Tracker.db')
                            cur = data.cursor()
                            cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":credit_cash,"Bank":credit_bank,"Credit":credit_bank+credit_cash,"Debit":0})
                            data.commit()
                            data.close()

                            data = sqlite3.connect("Tracker.db")
                            cur = data.cursor()
                            cur.execute("DELETE FROM Transaction_Record WHERE Day = :Day AND Month =:Month AND Year =:Year AND Amount = :Amount", {'Day':Day,'Month':Month,'Year':Year,'Amount':credit_bank+credit_cash})
                            data.commit()
                            data.close()
                            print("The transaction record has been deleted.")
                        else:
                            print("Invalid Operation! Please enter valid input...")   
                    elif mode == '4':
                        break
                    else:
                        print("Invalid Operation! Please enter valid input...")   
            else:
                print("Invalid Operation! Please enter valid input...")   
        else:
            print("Invalid Operation! Please enter valid input...")   

def expenditure():
    while True:
        user = input('''What would you like to view:
                     1. To view weekly expenditure details -> Press 1
                     2. To view monthly expenditure details -> Press 2
                     3. To view quarterly expenditure details -> Press 3
                     4. To view half-yearly expenditure details -> Press 4
                     5. To view yearly expenditure details -> Press 5
                     6. To exit to previous menu -> Press 6
                     ''')
        
        if user.isdigit() :
            user = int(user)
            today = datetime.now()
            if user == 1:
                start_date = today - timedelta(days=7)
            elif user == 2:
                start_date = today - timedelta(days=30)
            elif user == 3:
                start_date = today - timedelta(days=90)
            elif user == 4:
                start_date = today - timedelta(days=180)
            elif user == 5:
                start_date = today - timedelta(days=365)
            elif user == 6:
                break
            else:
                print("Invalid operation! Please give valid input...")


            data = sqlite3.connect('Tracker.db')
            cur = data.cursor()
            cur.execute("""
                SELECT Day, Month, Year, Amount, Category
                FROM Transaction_Record
                WHERE (Year = :start_year AND Month = :start_month AND Day >= :start_day)
                OR (Year = :today_year AND Month = :today_month AND Day <= :today_day)
                OR (Year = :start_year AND Month > :start_month)
                OR (Year = :today_year AND Month < :today_month)
                OR (Year > :start_year AND Year < :today_year)
                """, {
                'start_year': start_date.year,
                'start_month': start_date.month,
                'start_day': start_date.day,
                'today_year': today.year,
                'today_month': today.month,
                'today_day': today.day
            })

            result = cur.fetchall()
            if result:
                for row in result:
                    print(f"Date: {row[2]:04d}-{row[1]:02d}-{row[0]:02d}, Amount: {row[3]}, Category: {row[4]}")
                graph_input = input('''To view the history in graphical method -> Press 1
                                To exit -> Press any key''')
                if graph_input == '1':
                    graph(result)
            else:
                print("No records found.")
                break     
            
            break

        else:
            print("Invalid operation! Please give valid input...")

def wallet():
    while True:
        user = input('''What would you like to view in the wallet?
                        1. To credit money into the wallet -> Press 1
                        2. To debit money from the wallet -> Press 2
                        3. To view the amount of money in the wallet -> Press 3
                        4. To exit the wallet -> Press 4
                        \n''')

        if user.isdigit(): 
            user = int(user)
            
            if user == 1:
                medium = input('''Would you like to credit using cash or bank:
                                1. For cash -> Press 1
                                2. For bank transfer -> Press 2
                                3. To credit in both -> Press 3
                                4. To retun to previous menu -> Press 4
                                \n ''')
                
                if medium.isdigit():
                    medium = int(medium)

                    if medium == 1: 
                        credit = input("Please enter the amount to be credited (as cash): ")
                        if credit.isdigit():
                            credit = int(credit)
                            data = sqlite3.connect('Tracker.db')
                            cur = data.cursor()
                            cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":credit,"Bank":0,"Credit":credit,"Debit":0})

                            data.commit()
                            data.close()
                            
                        else:
                            print("Invalid amount! Please enter a valid number...")

                    elif medium == 2:
                        credit = input("Please enter the amount to be credited (as bank): ")
                        if credit.isdigit():
                            credit = int(credit)
                            data = sqlite3.connect('Tracker.db')
                            cur = data.cursor()
                            cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":0,"Bank":credit,"Credit":credit,"Debit":0})

                            data.commit()
                            data.close()
                        else:
                            print("Invalid amount! Please enter a valid number...")

                    elif medium == 3:
                        credit_cash = input("Please enter the amount to be credited in cash: ")
                        credit_bank = input("Please enter the amount to be credited in bank: ")
                        
                        if credit_cash.isdigit() and credit_bank.isdigit():
                            credit_cash = int(credit_cash)
                            credit_bank = int(credit_bank)
                            data = sqlite3.connect('Tracker.db')
                            cur = data.cursor()
                            cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":credit_cash,"Bank":credit_bank,"Credit":credit_cash+credit_bank,"Debit":0})

                            data.commit()
                            data.close()
                        else:
                            print("Invalid amount! Please enter valid numbers for cash and bank.")
                    elif medium == 4:
                        wallet()
                        break
                    else:
                        print("Invalid operation! Please choose a valid option...")

                else:
                    print("Invalid operation! Please enter a number...")

            elif user == 2:
                medium = input('''Would you like to debit using cash or bank:
                                1. From cash -> Press 1
                                2. From bank -> Press 2
                                3. To debit from both -> Press 3
                                4. To return to previous menu -> Press 4
                                \n ''')
                
                if medium.isdigit():
                    medium = int(medium)

                    if medium == 1: 
                        debit = input("Please enter the amount to be debited (as cash): ")
                        if debit.isdigit():
                            debit = int(debit)
                            data = sqlite3.connect('Tracker.db')
                            cur = data.cursor()
                            cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":0-debit,"Bank":0,"Credit":0,"Debit":debit})

                            data.commit()
                            data.close()
                        else:
                            print("Invalid amount! Please enter a valid number...")

                    elif medium == 2:
                        debit = input("Please enter the amount to be debited from bank: ")
                        if debit.isdigit():
                            debit = int(debit)
                            data = sqlite3.connect('Tracker.db')
                            cur = data.cursor()
                            cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":0,"Bank":0-debit,"Credit":0,"Debit":debit})

                            data.commit()
                            data.close()
                            
                        else:
                            print("Invalid amount! Please enter a valid number...")

                    elif medium == 3:
                        debit_cash = input("Please enter the amount to be debited in cash: ")
                        debit_bank = input("Please enter the amount to be debited in bank: ")
                        
                        if debit_cash.isdigit() and debit_bank.isdigit():
                            debit_cash = int(debit_cash)
                            debit_bank = int(debit_bank)
                            data = sqlite3.connect('Tracker.db')
                            cur = data.cursor()
                            cur.execute("INSERT INTO WALLET VALUES(:Day,:Month,:Year,:Cash,:Bank,:Credit,:Debit)",{"Day":datetime.now().day,"Month":datetime.now().month,"Year":datetime.now().year,"Cash":0-debit_cash,"Bank":0-debit_bank,"Credit":0,"Debit":debit_cash+debit_bank})

                            data.commit()
                            data.close()
                        else:
                            print("Invalid amount! Please enter valid numbers for cash and bank.")

                    elif medium == 4:
                        wallet()
                        break
                    else:
                        print("Invalid operation! Please choose a valid option...")

                else:
                    print("Invalid operation! Please enter a number...")

            elif user ==3:
                data = sqlite3.connect('Tracker.db')
                cur = data.cursor()
                cur.execute("SELECT SUM(Cash), SUM(Bank) FROM WALLET")

                data.commit()
                result = cur.fetchone()

                if result:
                    total_cash, total_bank = result
                    print(f"Cash: {total_cash}, Bank: {total_bank}, Total: {total_bank+total_cash}")
                else:
                    print("No data available.")
                data.close()

            elif user == 4:
                print("Exiting the wallet...")
                break
            else:
                print("Invalid operation! Please enter a valid option...")

def graph(result):

# defaultdict: A subclass of the built-in dict, this simplifies the code by avoiding key errors and automatically assigning an initial value (0) to keys that don’t exist yet.
# Key-Value Storage: Dates are stored as keys (date_key), and amounts are stored as values (grouped_data[date_key]). This allows efficient grouping of data based on the date.

    grouped_data =defaultdict(int)
    for row in result:
        day,month,year,amount,category = row
        data = f"{day:02d}-{month:02d}-{year:04d}"

        grouped_data[data] +=amount
    for date, total_amount in grouped_data.items():
        print(f"Date: {date}, Total Amount: {total_amount}")

    days = list(grouped_data.keys())
    amounts = list(grouped_data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(days, amounts, color='skyblue')
    plt.xlabel('Date')
    plt.ylabel('Total Expenditure')
    plt.title('Expenditure Grouped by Day')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()

def lend():
    while True:
        user = input('''___WELCOME TO MONEY LENDING TRACKER___
                    1. To check who you owe money -> Press 1
                    2. To add borrowed money record -> Press 2
                    3. To check if someone owes you money -> Press 3
                    4. To add lending money record -> Press 4
                    5. To return to previous menu -> Press 5
                     ''')
        if user.isdigit():
            user = int(user)
            if user == 1:
                data = sqlite3.connect('Tracker.db')
                cur = data.cursor()
                cur.execute("SELECT * FROM Lending_Record WHERE Lender = Borrowed")
                result = cur.fetchall()
                data.commit()
                cur.close()
                if result:
                    for row in result:
                        day,month,year,amount,name,category = row
                        print(f"Date: {year:04d}-{month:02d}-{day:02d}, Amount: {amount}, Name: {name}, Category: {category}")
                else:
                    print("No records found.")
            elif user == 2:
                data = sqlite3.connect('Tracker.db')
                cur = data.cursor()
                cur.execute("INSERT INTO Lending_Record VALUES(:Day,:Month,:Year,:Amount,:Name,:Lend,:Category)")
            elif user == 5:
                break
            else:
                print("Invalid amount! Please enter a valid number...")
        else:
            print("Invalid amount! Please enter a valid number...")
        
    

def delete():

    user = input('''Are you sure you want to delete all records? 
                 1. To continue -> Press 1
                 2. To cancel -> Press any key''')
    if user == '1':
        data = sqlite3.connect('Tracker.db')
        cur = data.cursor()
        cur.execute("DROP TABLE WALLET")
        data.commit()
        cur.execute("DROP TABLE Transaction_Record")
        data.commit()
        cur.close()
    else:
        pass


if __name__ == "__main__":
    while True:
        data = sqlite3.connect('Tracker.db')
        cur = data.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS WALLET
            (Day INTEGER,
             Month INTEGER,
             Year INTEGER,
             Cash INTEGER,
             Bank INTEGER,
             Credit INTEGER,
             Debit INTEGER)
            ''')
        data.commit()
        cur.execute('''CREATE TABLE IF NOT EXISTS Transaction_Record
            (Day INTEGER,
             Month INTEGER,
             Year INTEGER,
             Amount INTEGER,
             Category TEXT)
            ''')
        cur.execute('''CREATE TABLE IF NOT EXISTS Lending_Record
            (Day FLOAT,
             Month FLOAT,
             Year FLOAT,
             Amount FLOAT,
             Name TEXT,
             Lender TEXT,
             Category TEXT)
            ''')
        data.commit()
        cur.close()
        user = input('''_____WELCOME TO FINANCE TRACKER_____
                    Please choose the one of the following options to proceed
                    1. To add a financial record -> Press 1
                    2. To remove a financial record -> Press 2
                    3. To view detailed total expenditure -> Press 3
                    4. To view wallet -> Press 4
                    5. To open money lending tracker -> Press 5
                    6. To exit -> Press 6 
                    7. To delete all records -> Press 7    
                     \n''')
        if user.isdigit():
            user = int(user)
            if user == 1:
                add()
            elif user == 2:
                remove()
            elif user == 3:
                expenditure()
            elif user == 4:
                wallet()
            elif user == 5:
                lend()
            elif user == 6:
                print("_____THANK YOU FOR USING THE FINANCE TRACKER_____")
                break
            elif user ==7:
                delete()
        else:
            print("Invalid operation! Please try again...")

