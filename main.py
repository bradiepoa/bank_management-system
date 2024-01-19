import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root', password='', database='bank_management')
def OpenAcc():
    n = input("Enter Name: ")
    ac = input("Enter Account No: ")
    db = input("Enter date of birth: ")
    cn = input("Enter contact number: ")
    ob = int(input("Enter opening balance: "))
    add = input("Enter address: ")
    
    if ob < 2000:
        print("Opening balance should be 2000 at least. Account not created.")
    else:
        # Creating data for insertion into tables
        data1 = (n, ac, db, cn, ob, add)
        data2 = (n, ac, ob)

        # SQL statements for insertion
        sql1 = 'INSERT INTO account VALUES (%s, %s, %s, %s, %s, %s)'
        sql2 = 'INSERT INTO amount VALUES (%s, %s, %s)'

        # Database connection and cursor
        x = mydb.cursor()

        try:
            # Execute the SQL statements
            x.execute(sql1, data1)
            x.execute(sql2, data2)
            mydb.commit()

            print("Data submitted successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            x.close()

    main()

def  DespoAmo():
    account = input("Enter amount you want to deposit: ")
    ac=input("Enter Account No:  ")
    a='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    t=result[0] + int(account)
    sql = 'update amount set balance=%s where AccNo=%s'

    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def WithdrawAmount():
    account = input("Enter amount you want to withdraw: ")
    ac=input("Enter Account No:  ")
    a ='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    t=result[0] - int(account)
    sql = 'UPDATE amount SET balance=%s WHERE AccNo=%s'
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()
    
def BalEng():
    ac=input("Enter the account no: ")
    a='select * from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    print("Balance for account:", ac,"is", result[-1])
    main()

def DispDetails():
    ac=input("Enter the account no: ")
    a='select * from account where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    for i in result:
        print(i)
    main()

def CloseAcc():
    ac=input("Enter the account no: ")
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    mydb.commit()
    main()


def main():
    print('''
               1. OPEN NEW ACCOUNT
               2. DEPOSIT AMOUNT
               3. WITHDRAW AMOUNT
               4. BALANCD EQUITY
               5. DISPLAY CUSTOMER DETAILS
               6. CLOSE AN ACCOUNT''')
               
    choice = input("Enter the task you want to perform:  ")
    if (choice=='1'):
        OpenAcc()
    elif (choice=='2'):
        DespoAmo()
    elif (choice=='3'):
        WithdrawAmount()
    elif (choice=='4'):
        BalEng()
    elif (choice=='5'):
        DispDetails()
    elif (choice=='6'):
        CloseAcc()
    else:
        print("Invalid input please try again")
        main()
main()