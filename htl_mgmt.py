import mysql.connector as sql
from tabulate import tabulate
import sys


conn = sql.connect(host='localhost', user='root',
                   passwd='1234', database='hostel')
conn.autocommit = True
if conn.is_connected():
    print('connected succesfully')
else:
    print('not connected')

c1 = conn.cursor()
#c1.execute("create table fees(department int primary key,fees int)")


# c1.execute("create table hostel_management(roll_no int primary key,name varchar(20),address varchar(100),room_no int,dept varchar(15),fees int,bal int)


def data_insertion():

    roll_no = int(input("ENTER YOUR ROLL NUMBER : "))
    name = input("ENTER YOUR NAME : ")
    address = input("ENTER YOUR ADDRESS : ")

    room_no = int(input("ENTER YOUR ROOM NUMBER : "))

    dept = input("ENTER YOUR DEPARTMENT : ")
    fees = int(input("ENTER YOUR FEES : "))
    balance = int(input("ENTER YOUR BALANCE : "))
    details = [roll_no, name, address, room_no, dept, fees, balance]

    abc = "insert into hostel_management_table(roll_no,name,address,room_no,dept,fees,balance)values(%s,%s,%s,%s,%s,%s,%s)"

    c1.execute(abc, details)
    conn.commit()


def data_extraction():

    print(""" Search criteria : 
            1. Roll No
            2. Name
            3. Room No
            4. Departement
            5. All""")

    ch = int(input("Enter your choice : "))

    if ch == 1:
        roll_no = int(input("enter your roll number"))
        mysql = "select*from hostel_management_table where roll_no={}".format(
            roll_no)
        c1.execute(mysql)
        data = c1.fetchall()

    elif ch == 2:
        name = int(input("enter your name "))
        mysql = "select*from hostel_management_table where name={}".format(
            name)
        c1.execute(mysql)
        data = c1.fetchall()

    elif ch == 3:
        room_no = int(input("enter your room number"))
        mysql = "select*from hostel_management_table where room_no={}".format(
            room_no)
        c1.execute(mysql)
        data = c1.fetchall()

    elif ch == 4:

        print("AVAILABLE DEPARTMENTS AS FOLLOWS")
        print("         1.COMPUTER")
        print("         2.BIO")
        print("         3.TECH")
        print("         4.PHYSICS")
        print("         5.ECO")
        print("         6.ENG")
        department = input("enter your department").lower()
        mysql = "select*from hostel_management_table where dept={}".format(
            department)
        c1.execute(mysql)
        data = c1.fetchall()

    elif ch == 5:
        mysql = "select*from hostel_management_table"
        c1.execute(mysql)
        data = c1.fetchall()

    else:
        print('unknown option')

    for data2 in data:
        print(data2)


def remove_std():

    user_input = int(input("Enter the roll no you want to remove: "))
    sql = "Delete from hostel_management_table where roll_no ={}".format(
        user_input)
    c1.execute(sql)
    print("Admission has been removed successfully")


while True:
    print("                                   WELCOME TO  HOSTEL MANAGEMENT                                   ")

    print("     1.ADMISSION FORM")

    print("     2.FEE CHECKING")

    print("     3.REMOVE ADMISSION")

    print("     4.QUIT")
    choice = int(input('ENTER YOUR CHOICE'))
    if choice == 1:
        data_insertion()

    elif choice == 2:
        data_extraction()

    elif choice == 3:
        remove_std()

    else:
        print("QUITTING!!!!!!!!!")
        sys.exit()
