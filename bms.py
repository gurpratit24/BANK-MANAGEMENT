from datetime import datetime
import mysql.connector
cn=mysql.connector.connect(host='localhost',user='root',password='12345678',database='bank')
mycursor=cn.cursor()
logo = """


  ____              _      __  __                                                   _   
 |  _ \            | |    |  \/  |                                                 | |  
 | |_) | __ _ _ __ | | __ | \  / | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ 
 |  _ < / _` | '_ \| |/ / | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
 | |_) | (_| | | | |   <  | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ 
 |____/ \__,_|_| |_|_|\_\ |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
                                                     __/ |                              
                                                    |___/



                                                    """

def line(c='-',l=100):
        print(c*l)

def getlastcid():
    sql = "Select ifnull(max(cid),0) from customer"
    mycursor.execute(sql)
    records = mycursor.fetchall()
    if records[0][0]==0:
        return 1001
    return records[0][0]+1

def getlasttid():
    sql = "Select ifnull(max(tid),0) from transaction"
    mycursor.execute(sql)
    records = mycursor.fetchall()
    if records[0][0]==0:
        return 1984
    return records[0][0]+1

def add_cust():
    rec=[]
    while True:
        customerid=getlastcid()
        print("Customer ID : ",customerid)
        cname = input("Enter customer name ")
        dob= input(" Enter date of birth (yyyy/mm/dd)")
        address = input("Enter your address ")
        phone = int(input("Enter your phone number "))
        email = input("Enter your email address")
        atype = input("Enter type of account (c/s)")
        balance = int(input("Enter the Initial Deposit "))
        pwd = input("Choose Password : ")
        rec=[customerid,cname,dob,address,phone,email,atype,balance,pwd]
        sql="insert into customer(cid,cname,dob,address,phone,email,atype,balance,password) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,rec)
        cn.commit()
        print("Insertion Done...")
    
        ch = input("Press 'x' to exit, any other key to continue... ")
        if ch=='x' or ch=='X' : break

def show_cust():
    sql = "Select * from Customer"
    mycursor.execute(sql)
    records = mycursor.fetchall()
    if len(records)==0:
        print(" No Record found...")
        return
    line("-",115)
    print('\tCustID\tCust Name\tBirth Date\tAddress\t\tPhone\t\tEmail\t\tType\tBalance')
    line("-",115)
    for rec in records :
        print('{:14}'.format(rec[0]),'{:15}'.format(rec[1]),'{:12}'.format(str(rec[2])),'{:20}'.format(rec[3]),'{:12}'.format(rec[4]),'{:20}'.format(rec[5]),'{:5}'.format(rec[6]),'{:10}'.format(rec[7]))
    line("=",115)
   

def search_custid():
    cid=int(input("Enter customer id : "))
    sql = "Select * from customer where cid="+str(cid)
    mycursor.execute(sql)
    records = mycursor.fetchall()
    if len(records)==0:
        print("Record not found...")
        return
    line("-",115)
    print('\tCustID\tCust Name\tBirth Date\tAddress\t\tPhone\t\tEmail\t\tType\tBalance')
    line("-",115)
    for rec in records:
        print('{:14}'.format(rec[0]),'{:15}'.format(rec[1]),'{:12}'.format(str(rec[2])),'{:20}'.format(rec[3]),'{:12}'.format(rec[4]),'{:20}'.format(rec[5]),'{:5}'.format(rec[6]),'{:10}'.format(rec[7]))
    line("=",115)

def show_balance(records):
    line("-",115)
    print('\tCustID\tCust Name\tBirth Date\tAddress\t\tPhone\t\tEmail\t\tType\tBalance')
    line("-",115)
    for rec in records:
        print('{:14}'.format(rec[0]),'{:15}'.format(rec[1]),'{:12}'.format(str(rec[2])),'{:20}'.format(rec[3]),'{:12}'.format(rec[4]),'{:20}'.format(rec[5]),'{:5}'.format(rec[6]),'{:10}'.format(rec[7]))
    line("=",115)


def search_custname() :
    name = input("Enter cname : ")
    sql = "Select * from customer where cname='"+str(name)+"'"
    mycursor.execute(sql)
    records = mycursor.fetchall()
    if len(records)==0:
        print("Record not found...")
        return
    line("-",115)
    print('\tCustID\tCust Name\tBirth Date\tAddress\t\tPhone\t\tEmail\t\tType\tBalance')
    line("-",115)
    for rec in records:
        print('{:14}'.format(rec[0]),'{:15}'.format(rec[1]),'{:12}'.format(str(rec[2])),'{:20}'.format(rec[3]),'{:12}'.format(rec[4]),'{:20}'.format(rec[5]),'{:5}'.format(rec[6]),'{:10}'.format(rec[7]))
    line("=",115)

        
def update_address():
    N=input("Enter the customer id where you want to update : ")
    mycursor.execute("Select * from customer where CID ="+N)
    row=mycursor.fetchall()
    if len(row)==0:
        print("Customer Id does not exist...")
        return 
    print("Existing Address : ",row[0][3])
    ch=input("Do you want to change the address {Y/N} : ")
    if ch=='y' or ch=='Y':
        new=input("Enter the New Address : ")
        query2="update customer set ADDRESS='"+new+"' where cid="+N
        mycursor.execute(query2)
        cn.commit()
        print("Record Updated...")

def update_address_user(row):
    print("Existing Address : ",row[0][3])
    ch=input("Do you want to change the address {Y/N} : ")
    if ch=='y' or ch=='Y':
        new=input("Enter the New Address : ")
        query2="update customer set ADDRESS='"+new+"' where cid="+str(row[0][0])
        mycursor.execute(query2)
        cn.commit()
        print("Record Updated...")
        mycursor.execute("Select * from customer where CID ="+str(row[0][0]))
        row=mycursor.fetchall()
        return row

def update_phone():
    N=input("Enter the customer id where you want to update : ")
    mycursor.execute("Select * from customer where CID="+N)
    row=mycursor.fetchall()
    if len(row)==0:
        print("Customer Id does not exist...")
        return 
    print("old phone no. = ",row[0][4])
    ch=input("Do you want to change the phone number {Y/N}")
    if ch=='y' or ch =='Y':
        new=input("Enter the new phone number : ")
        query2="update customer set PHONE = "+new+" where CID="+N
        mycursor.execute(query2)
        cn.commit()
        print("Record Updated...")

def update_phone_user(row):
    print("old phone no. = ",row[0][4])
    ch=input("Do you want to change the phone number {Y/N}")
    if ch=='y' or ch =='Y':
        new=input("Enter the new phone number : ")
        query2="update customer set PHONE = "+new+" where CID="+str(row[0][0])
        mycursor.execute(query2)
        cn.commit()
        print("Record Updated...")
        mycursor.execute("Select * from customer where CID ="+str(row[0][0]))
        row=mycursor.fetchall()
        return row

def delete():
    N=input("Enter the customer id where you want to delete")
    query1="Select * from customer where CID="+N
    mycursor.execute(query1)
    row=mycursor.fetchall()
    if len(row)==0:
        print("Customer Id does not exist")
        return
    print(row)
    ch=input("Do you want to delete this record {Y/N}? ")
    if ch=='y' or ch=='Y':
        query2="Delete from customer where Cid="+N
        mycursor.execute(query2)
        cn.commit()
        print("Record Deleted...")
        

def deposit():
    cdatetime=datetime.now()
    print("Current Date Time is : ",cdatetime)
    cid = int(input("Enter Customer ID for Deposit : "))
    sql = "Select * from customer where CID = "+str(cid)
    mycursor.execute(sql)
    records = mycursor.fetchall()
    if len(records)==0:
        print("Invalid Customer Id.... ")
        return
    amt = float(input("Enter Amount to Deposit : "))
    tid=getlasttid()
    sql = "Insert into Transaction (tid, tdate, cid, amount, ttype) values ("+str(tid)+",'"+str(cdatetime)+"',"+str(cid)+","+str(amt)+",'D')"
    mycursor.execute(sql)
    cn.commit()
    sql = "Update Customer set balance = balance + "+str(amt)+" where cid = "+str(cid)
    mycursor.execute(sql)
    cn.commit()
    print("Deposit successful with Transaction id "+str(tid)+"...")

def deposit_user(records):
        cdatetime=datetime.now()
        print("Current Date Time is : ",cdatetime)
        amt = float(input("Enter Amount to Deposit : "))
        tid=getlasttid()
        sql = "Insert into Transaction (tid, tdate,cid, amount, ttype) values ("+str(tid)+",'"+str(cdatetime)+"',"+str(records[0][0])+","+str(amt)+",'D')"
        mycursor.execute(sql)
        cn.commit()
        sql = "Update Customer set balance = balance + "+str(amt)+" where cid = "+str(records[0][0])
        mycursor.execute(sql)
        cn.commit()
        print("Deposit successful with Transaction id "+str(tid)+"...")
        mycursor.execute("Select * from customer where CID ="+str(records[0][0]))
        records=mycursor.fetchall()
        return records

    
def withdraw():
        cdatetime=datetime.now()
        print("Current Date Time is : ",cdatetime)
        cid = int(input("Enter Customer ID : "))
        sql = "Select * from customer where cid = " + str(cid)
        mycursor.execute(sql)
        record = mycursor.fetchall()
        if len(record)==0:
                print("Invalid Customer ID ....")
                return
        while 1:
                amt=float(input("Enter Amount to Withdraw : "))
                if amt>record[0][7]:
                        print("Insufficient Balance, Current Balance is  ",record[0][7],"...")
                        ch = input("Wants to retry ... ")
                        if ch=='y' or ch=='Y':
                                continue
                        else : break
                break
        tid = getlasttid()
        sql = "insert into Transaction (tid,tdate,cid,amount,ttype) values ("+str(tid)+",'"+str(cdatetime)+"',"+str(cid)+","+str(amt)+",'W')"
        mycursor.execute(sql)
        cn.commit()
        sql = "Update Customer set balance = balance-"+str(amt)+" where cid ="+str(cid)
        mycursor.execute(sql)
        cn.commit()
        print("Withdrawal done with Transaction ID :",tid,"...")

def withdraw_user(record):
        cdatetime=datetime.now()
        print("Current Date Time is : ",cdatetime)
        while 1:
                amt=float(input("Enter Amount to Withdraw : "))
                if amt>record[0][7]:
                        print("Insufficient Balance, Current Balance is  ",record[0][7],"...")
                        ch = input("Wants to retry ... ")
                        if ch=='y' or ch=='Y':
                                continue
                        else : break
                break
        tid = getlasttid()
        sql = "insert into Transaction (tid,tdate,cid,amount,ttype) values ("+str(tid)+",'"+str(cdatetime)+"',"+str(record[0][0])+","+str(amt)+",'W')"
        mycursor.execute(sql)
        cn.commit()
        sql = "Update Customer set balance = balance-"+str(amt)+" where cid ="+str(record[0][0])
        mycursor.execute(sql)
        cn.commit()
        print("Withdrawal done with Transaction ID :",tid,"...")
        mycursor.execute("Select * from customer where CID ="+str(record[0][0]))
        record=mycursor.fetchall()
        return record

def login():
        print(logo,"\n\n")
        while 1 :
                user = input("Enter Customer ID :")
                password = input("Enter Password : ")
                sql = "select * from customer where cid = '"+user+"'"
                mycursor.execute(sql)
                record=mycursor.fetchall()
                if user.upper()=="ADMIN" and password=="qwertyuiop":
                        admin_main()
                        break
                elif len(record)==0:
                        print("Invalid Customer ID, please re-enter...")
                elif password.upper()==record[0][8]:
                        user_main(record)
                        break
                else:
                        print("Invalid password ...")
                
def admin_main():
        
    while True:
        
        print("\n",logo)
        print("1. Add Customer")
        print("2. Show All")
        print("3. Search by Cust ID")
        print("4. Search by Cust name ")
        print("5. Update address ")
        print("6. Update phone number")
        print("7. Delete Record")
        print("8. Deposit")
        print("9. Withdrawal")
        print("0. Exit")
        
        ch=input("Enter Your Choice...{0-9}:")
        if ch=='1' :
            add_cust()
        elif ch=='2' :
            show_cust()
        elif ch=='3' :
            search_custid()
        elif ch=='4' :
            search_custname()
        elif ch=='5' :
            update_address()
        elif ch=='6' :
            update_phone()
        elif ch=='7' :
            delete()
        elif ch=='8' :
            deposit()
        elif ch=='9' :
            withdraw()            
        elif ch=='0' :
            break
        else:
            print("Invalid Choice...")

def user_main(record):
        
    while True:
        print("\n",logo)
        print("1. Show Current Balance")
        print("2. Update address ")
        print("3. Update phone number")
        print("4. Deposit")
        print("5. Withdrawal")
        print("0. Exit")
        
        ch=input("Enter Your Choice...{0-5}:")
        if ch=='1':
            show_balance(record)
        elif ch=='2':
            record=update_address_user(record)
        elif ch=='3':
            record=update_phone_user(record)
        elif ch=='4' :
            record=deposit_user(record)
        elif ch=='5' :
            record=withdraw_user(record)            
        elif ch=='0':
            break
        else:
            print("Invalid Choice...")
            
login()
