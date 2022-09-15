import re
import mysql.connector

# making Connection
con = mysql.connector.connect(
    host='localhost', user='root',password = '28122001')

# preparing a cursor object
cursorObject = con.cursor()
 
# creating database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS employee")

# selecting employee database
cursorObject.execute("USE employee")

# creating table
cursorObject.execute("CREATE TABLE IF NOT EXISTS empdata (Id INT(11) PRIMARY KEY, Name VARCHAR(255), Email_Id VARCHAR(255), Phone_no BIGINT(11), Address VARCHAR(1800), Post VARCHAR(20), Salary BIGINT(10)) ")

# make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# for validating an Phone Number
Pattern = re.compile("(0|91)?[6-9][0-9]{9}")


# Function to Add_Employ
def Add_Employ():
    print("{:>60}".format("-->>Add Employee Record<<--"))
    
    Id = input("Enter Employee Id: ")
    if (check_employee(Id) == True):
        print("Employee ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
        
    Name = input("Enter Employee Name: ")
        
    Email_Id = input("Enter Employee Email ID: ")
    if(re.fullmatch(regex, Email_Id)):
        print("Valid Email")
        if (check_employee_email(Email_Id)==True):
            print("Employee Email Id Already Exists\nTry Again..")
            press = input("Press Any Key To Continue..")
            Add_Employ()  
    else:
        print("Invalid Email")
        press = input("Press Any Key To Continue..")
        Add_Employ()
        
    Phone_no = input("Enter Employee Phone No.: ")
    if(Pattern.match(Phone_no)):
        print("Valid Phone Number")
        if (check_employee_phone(Phone_no)==True):
            print("Employee Phone Number Already Exists\nTry Again..")
            press = input("Press Any Key To Continue..")
            Add_Employ()
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key To Continue..")
        Add_Employ()
        
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)

    sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()

    c.execute(sql, data)

    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    menu()

#Function To Check if Employee With given Id Exist or not
def check_employee(employee_id):

    sql = 'select * from empdata where Id=%s'
    
    c = con.cursor(buffered=True)
    data = (employee_id,)

    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

# Function To Check if Employee With given Email Id Exist or not
def check_employee_email(email_id):

    sql = 'select * from empdata where Email_Id=%s'
    
    c = con.cursor(buffered=True)
    data = (email_id,)

    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
# Function To Check if Employee With given Phone Number Exist or not     
def check_employee_phone(phone_no):

    sql = 'select * from empdata where Phone_no=%s'
    
    c = con.cursor(buffered=True)
    data = (phone_no,)

    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

# Function to Display_Employ
def Display_Employ():
    print("{:>60}".format("-->> Display Employee Record <<--"))
    
    l=int(input('Do you want to limit the data ? (1 for Yes, 0 for No) '))
    if l==0:
        s=int(input('Do you want to sort the Data ? (1 for Yes, 0 for No)  '))
        if s==0:

            sql = 'select * from empdata'
            c = con.cursor()

            c.execute(sql)

            r = c.fetchall()
            for i in r:
                print("Employee Id: ", i[0])
                print("Employee Name: ", i[1])
                print("Employee Email Id: ", i[2])
                print("Employee Phone No.: ", i[3])
                print("Employee Address: ", i[4])
                print("Employee Post: ", i[5])
                print("Employee Salary: ", i[6])
                print("\n")
        
        elif s==1:
            sort=int(input('From which column you want to sort the data ? (1 for Id, 2 for Name, 3 for Salary)'))
            asc=int(input('Do you want to sort ascending or descending ? (1 for ascending, 2 for descending)'))
            if asc == 1:
                if sort == 1:
                    sql='select * from empdata order by id'
                elif sort == 2 :
                    sql='select * from empdata order by name'
                elif sort==3:
                    sql='select * from empdata order by salary'
                    
                
                c = con.cursor()

                c.execute(sql)

                r = c.fetchall()
                for i in r:
                    print("Employee Id: ", i[0])
                    print("Employee Name: ", i[1])
                    print("Employee Email Id: ", i[2])
                    print("Employee Phone No.: ", i[3])
                    print("Employee Address: ", i[4])
                    print("Employee Post: ", i[5])
                    print("Employee Salary: ", i[6])
                    print("\n")
            elif asc == 2:
                
                if sort == 1:
                    sql='select * from empdata order by id desc'
                elif sort == 2 :
                    sql='select * from empdata order by name desc'
                elif sort==3:
                    sql='select * from empdata order by salary desc'
                
                c = con.cursor()

                c.execute(sql)

                r = c.fetchall()
                for i in r:
                    print("Employee Id: ", i[0])
                    print("Employee Name: ", i[1])
                    print("Employee Email Id: ", i[2])
                    print("Employee Phone No.: ", i[3])
                    print("Employee Address: ", i[4])
                    print("Employee Post: ", i[5])
                    print("Employee Salary: ", i[6])
                    print("\n")
                
    
    elif l==1:
        lim=int(input('Enter no of Records Nedded.'))
        lim=(lim,)
        s=int(input('Do you want to sort the Data ? (1 for Yes, 0 for No)  '))
        if s==0:

            sql = 'select * from empdata limit %s'
            c = con.cursor()

            c.execute(sql,lim)

            r = c.fetchall()
            for i in r:
                print("Employee Id: ", i[0])
                print("Employee Name: ", i[1])
                print("Employee Email Id: ", i[2])
                print("Employee Phone No.: ", i[3])
                print("Employee Address: ", i[4])
                print("Employee Post: ", i[5])
                print("Employee Salary: ", i[6])
                print("\n")
        
        elif s==1:
            sort=int(input('From which column you want to sort the data ? (1 for Id, 2 for Name, 3 for Salary)'))
            asc=int(input('Do you want to sort ascending or descending ? (1 for ascending, 2 for descending)'))
            if asc == 1:
                if sort == 1:
                    sql='select * from empdata order by id limit %s'
                elif sort == 2 :
                    sql='select * from empdata order by name limit %s'
                elif sort==3:
                    sql='select * from empdata order by salary limit %s'
                    
                
                c = con.cursor()

                c.execute(sql,lim)

                r = c.fetchall()
                for i in r:
                    print("Employee Id: ", i[0])
                    print("Employee Name: ", i[1])
                    print("Employee Email Id: ", i[2])
                    print("Employee Phone No.: ", i[3])
                    print("Employee Address: ", i[4])
                    print("Employee Post: ", i[5])
                    print("Employee Salary: ", i[6])
                    print("\n")
            elif asc == 2:
                
                if sort == 1:
                    sql='select * from empdata order by id desc limit %s'
                elif sort == 2 :
                    sql='select * from empdata order by name desc limit %s'
                elif sort==3:
                    sql='select * from empdata order by salary desc limit %s'
                
                c = con.cursor()

                c.execute(sql,lim)

                r = c.fetchall()
                for i in r:
                    print("Employee Id: ", i[0])
                    print("Employee Name: ", i[1])
                    print("Employee Email Id: ", i[2])
                    print("Employee Phone No.: ", i[3])
                    print("Employee Address: ", i[4])
                    print("Employee Post: ", i[5])
                    print("Employee Salary: ", i[6])
                    print("\n")
        
    press = input("Press Any key To Continue..")
    menu()
    
# Function to Update_Employ
def Update_Employ():
    print("{:>60}".format("-->> Update Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    sq='select * from empdata where Id=%s'
    d=(Id,)
    co=con.cursor()
    co.execute(sq,d)
    i=co.fetchone()

    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        print('Employee Current Name : ',i[1])
        Name=input('Enter Employee New Name : ')
        
        print('Employee Current Email ID : ',i[2])
        Email_Id = input("Enter Employee New Email ID : ")
        if(re.fullmatch(regex, Email_Id)):
            print("Valid Email")
        else:
            print("Invalid Email")
            press = input("Press Any Key To Continue..")
            Update_Employ()
            
        print('Employee Current Phone No. : ',i[3])
        Phone_no = input("Enter Employee Phone No. : ")
        if(Pattern.match(Phone_no)):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
            press = input("Press Any Key To Continue..")
            Update_Employ()
            
        print('Employee Current Address : ',i[4])    
        Address = input("Enter Employee Address: ")

        sql = 'UPDATE empdata set Name = %s ,Email_Id = %s, Phone_no = %s, Address = %s where Id = %s'
        data = (Name,Email_Id, Phone_no, Address, Id)
        c = con.cursor()

        c.execute(sql, data)

        con.commit()
        print("Updated Employee Record")
        press = input("Press Any Key To Continue..")
        menu()
        
# Function to Promote_Employ
def Promote_Employ():
    print("{:>60}".format("-->> Promote Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")

    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
        
    else:
        
        sql = 'select * from empdata where Id=%s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        i = c.fetchone()
        print('Employee Current Post : ',i[5])
        post  = (input("Enter New Post: "))
        print('Employee Current Salary : ',i[6])
        Amount  = int(input("Enter Increment Percent in Salary: "))
        
        t = i[6]+i[6]*Amount/100

        sql = 'update empdata set Salary = %s,Post = %s where Id = %s'
        d = (t,post, Id)

        c.execute(sql, d)

        con.commit()
        print("Employee Promoted")
        press = input("Press Any key To Continue..")
        menu()
        
# Function to Remove_Employ
def Remove_Employ():
    print("{:>60}".format("-->> Remove Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")

    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        sql = 'delete from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        con.commit()
        print("Employee Removed")
        press = input("Press Any key To Continue..")
        menu()
        
# Function to Search_Employ
def Search_Employ():
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")

    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        sql = 'select * from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email Id: ", i[2])
            print("Employee Phone No.: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary: ", i[6])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()

# Menu function to display menu
def menu():
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Display_Employ()
    elif ch == 3:
        Update_Employ()
    elif ch == 4:
        Promote_Employ()
    elif ch == 5:
        Remove_Employ()
    elif ch == 6:
        Search_Employ()
    elif ch == 7:
        print("{:>60}".format("See You Soon."))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()
        
menu()
