
# SOURCE CODE FOR LIBRARY

print("""****************************
*                          *
****   LIBRARY CODES    ****    
*                          *
****************************""")


#CREATING DATABASE

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists library")
mycursor.execute("use library")

#CREATING REQUIRED TABLES

mycursor.execute("create table if not exists library_master(cardno char(10) primary key,name_of_person varchar(30),phone_no char(10),address varchar(30),dob date)")
mycursor.execute("create table if not exists books(book_name varchar(30),book_no char(5) primary key,genre varchar(10),authors_name varchar(15),language varchar(15))")
mycursor.execute("create table if not exists library_transaction(cardno char(10),foreign key(cardno) references library_master(cardno),book_name varchar(20),date_of_lend date,date_of_return date)") 
mycursor.execute("create table if not exists buy_new_books(orderno varchar(6) primary key,name_of_book varchar(20),del_date date,price char(4))")
mydb.commit()

while True:
    
    print("""***************
1=create a new account
***************""")
    
    print("""***************
2=see the account info
***************""")
    
    print("""***************
3=update card holder info
***************""")
    
    print("""***************
4=delete the account
***************""")
    
    print("""***************
5=add new book
***************""")
    
    print("""***************
6=see books
***************""")
    
    print("""***************
7=update book details
***************""")
    
    print("""***************
8=delete book
***************""")
    
    print("""***************
9=lend a book
***************""")
    
    print("""***************
10=return the book
***************""")
    
    print("""***************
11=display lending history
***************""")
    
    print("""***************
12=order a new book
***************""")
    
    print("""***************
13=update order details
***************""")
    
    print("""***************
14=display ordering history
***************""")
    
    print("""***************
15=EXIT
***************""")
    
    ch=int(input("enter your choice"))


#TO CREATE A LIBRARY ACCOUNT
    if ch==1:
        print("if you wanna go back press  1")
        print(" ")
        print("if you wanna continue press  2")
        print(" ")
        a=int(input("enter your choice:"))
        if a==1:
            continue
        if a==2:
            print("FILL ALL PERSONAL DETAILS OF ACCOUNT HOLDER")
            cardno=str(input("enter card no:"))
            name_of_person=str(input("Enter name (limit 30 characters):"))
            phone_no=str(input("Enter phone no:"))
            address=str(input("Enter the address (max 30 words):"))
            dob=str(input("Enter the date of birth(yyyy-mm-dd):"))
            mycursor.execute("insert into library_master values('"+cardno+"','"+name_of_person+"','"+phone_no+"','"+address+"','"+dob+"')")
            mydb.commit()
            print("ACCOUNT IS SUCCESSFULLY CREATED!!!")
            
#TO SEE DETAILS OF CARD HOLDER
            
    if ch==2:
        cardno=str(input("Enter card no:"))
        mycursor.execute("select  *  from library_master where cardno='"+cardno+"'")
        for i in mycursor:
            print(i)
            
#TO UPDATE CARD HOLDER INFORMATION
            
    if ch==3:
        print("press 1 to update name:")
        print(" ")
        print("press 2 to update phone no:")
        print(" ")
        print("press 3 to update address:")
        print(" ")
        print("press 4 to update date of birth:")
        print(" ")
        ch1=int(input("Enter your choice:"))
        
#TO UPDATE NAME
        
        if ch1==1:
            mycursor.execute("select * from library_master")
            for i in mycursor:
                print(i)
            cardno=str(input("Enter card no:"))
            name_of_person=str(input("Enter new name:"))
            mycursor.execute("update library_master set name_of_person='"+name_of_person+"' where cardno='"+cardno+"'")
            mydb.commit()
            print("*Name has been updated*")
            mycursor.execute("select * from library_master")
            for i in mycursor:
                print(i)
                
#TO UPDATE PHONE NUMBER
                
        if ch1==2:
            mycursor.execute("select * from library_master")
            for i in mycursor:
                print(i)
            cardno=str(input("Enter card no:"))
            phone_no=str(input("Enter new phone no:"))
            mycursor.execute("update library_master set phone_no='"+phone_no+"' where cardno='"+cardno+"'")
            mydb.commit()
            print("*Number has been updated*")
            mycursor.execute("select * from library_master")
            for i in mycursor:
                print(i)
                
#TO UPDATE ADDRESS

        if ch1==3:
            mycursor.execute("select * from library_master")
            for i in mycursor:
                print(i)
            cardno=str(input("Enter card no:"))
            address=str(input("Enter new address:"))
            mycursor.execute("update library_master set address='"+address+"' where cardno='"+cardno+"'")
            mydb.commit()
            print("*Address has been updated*")
            mycursor.execute("select * from library_master")
            for i in mycursor:
                print(i)

#TO UPDATE DATE OF BIRTH
                
        if ch1==4:
            mycursor.execute("select * from library_master")
            for i in mycursor:
                print(i)
            cardno=str(input("Enter card no:"))
            dob=str(input("Enter new date of birth(yyyy-mm-dd):"))
            mycursor.execute("update library_master set dob='"+dob+"' where cardno='"+cardno+"'")
            mydb.commit()
            print("*Date of birth has been updated*")
            mycursor.execute("select * from library_master")
            for i in mycursor:
                print(i)
                
#TO DELETE AN ACCOUNT
                
    if ch==4:
        mycursor.execute("select * from library_master")
        for i in mycursor:
                print(i)
        cardno=str(input("Enter card no:"))
        mycursor.execute("delete from library_master where cardno='"+cardno+"'")
        mydb.commit()
        print("*Removed succesfully*")
        mycursor.execute("select * from library_master")
        for i in mycursor:
                print(i)
                
#TO ADD NEW BOOK
                
    if ch==5:
        print("FILL ALL BOOK DETAILS ")
        book_name=str(input("enter book  name:"))
        book_no=str(input("Enter no (limit 5 characters):"))
        genre=str(input("Enter genre:"))
        authors_name=str(input("Enter the authors name (max 15 words):"))
        language=str(input("Enter the language of book:"))
        mycursor.execute("insert into books values('"+book_name+"','"+book_no+"','"+genre+"','"+authors_name+"','"+language+"')")
        mydb.commit()
        print("Book added  succesfully*")
        for i in mycursor:
            print(i)
        
#TO SEE BOOK DETAILS
        
    if ch==6:
        book_no=str(input("Enter Book No:"))
        mycursor.execute("select  *  from books where book_no='"+book_no+"'")
        for i in mycursor:
            print(i)
            
#TO UPDATE BOOK DETAILS
            
    if ch==7:
        print("press 1 to update Book name")
        print(" ")
        print("press 2 to update genre")
        print(" ")
        print("press 3 to update Author Name")
        print(" ")
        print("press 4 to update Language")
        print(" ")
        ch1=int(input("Enter your choice:"))
        if ch1==1:
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
            book_no=str(input("Enter bookno:"))
            name_of_book=str(input("Enter new name:"))
            mycursor.execute("update books set book_name='"+name_of_book+"' where book_no='"+book_no+"'")
            mydb.commit()
            print("*Name has been updated*")
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
                
#TO UPDATE GENRE

                
        if ch1==2:
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
            book_no=str(input("Enter card no:"))
            genre=str(input("Enter new genre:"))
            mycursor.execute("update books set genre='"+genre+"' where book_no='"+book_no+"'")
            mydb.commit()
            print("*Genre has been updated*")
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
                
#TO UPDATE AUTHOR NAME
                
        if ch1==3:
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
            book_no=str(input("Enter book no:"))
            author=str(input("Enter new authors name:"))
            mycursor.execute("update books set authors_name='"+author+"' where book_no='"+book_no+"'")
            mydb.commit()
            print("*Authors name has been updated*")
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
                
#TO UPDATE LANGUAGE
                
        if ch1==4:
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
            book_no=str(input("Enter boom no:"))
            language=str(input("Enter new language:"))
            mycursor.execute("update books set language='"+language+"' where book_no='"+book_no+"'")
            mydb.commit()
            print("*Language has been updated*")
            mycursor.execute("select * from books")
            for i in mycursor:
                print(i)
                
#TO DELETE A BOOK
                
    if ch==8:
        mycursor.execute("select * from books")
        for i in mycursor:
            print(i)
        book_no=str(input("Enter book no:"))
        mycursor.execute("delete from books where book_no='"+book_no+"'")
        mydb.commit()
        print("*Removed succesfully*")
        mycursor.execute("select * from books")
        for i in mycursor:
            print(i)
            
#TO LEND A BOOK
            
    if ch==9:
        print("if you wanna go back press 1")
        print(" ")
        print("if you wanna coontinue press 2")
        print(" ")
        a=int(input("enter your choice:"))
        if a==1:
            continue
        if a==2:
            cardno=str(input("Enter card no:"))
            book_name=str(input("Enter the name of the book:"))
            date_of_lend=str(input("Enter date of lending(yyyy-mm-dd)"))
            print("if book not returned then enter(0000-00-00):")
            date_of_return=str(input("enter date of return(yyyy-mm-dd):"))    
            mycursor.execute("insert into library_transaction values('"+cardno+"','"+book_name+"','"+date_of_lend+"','"+date_of_return+"')")
            mydb.commit()
            
#TO RETURN A BOOK
            
    if ch==10:
        print("if you wanna go back press 1")
        print(" ")
        print("if you wanna coontinue press 2")
        print(" ")
        a=int(input("enter your choice:"))
        if (a==1):
            continue
        if a==2:
            cardno=str(input("Enter card no:"))
            date_of_return=str(input("Enter date of returning(yyyy-mm-dd):"))
            mycursor.execute("update library_transaction set date_of_return='"+date_of_return+"' where cardno='"+cardno+"'")
            mydb.commit()
            
#TO SEE LENDING HISTORY
            
    if ch==11:
        cardno=str(input("Enter card no:"))
        mycursor.execute("select  *  from library_transaction where cardno='"+cardno+"'")
        for i in mycursor:
         print(i)
            
#TO ORDER A NEW BOOK

    if ch==12:
        orderno=str(input("Enter the order no:"))
        name_of_book=str(input("Enter the name of the book:"))
        del_date=str(input("enter the expected delivery date of books(yyyy-mm-dd):"))
        price=str(input("Enter the price of the book"))
        mycursor.execute("insert into buy_new_books values('"+orderno+"','"+name_of_book+"','"+del_date+"','"+price+"')")
        mydb.commit()
        
#TO UPDATE ORDER DETAILS        

    if ch==13:
        print("press 1 to update name of book")
        print(" ") 
        print("press 2 to update delivery date")
        print(" ")
        print("press 3 to update price")
        print(" ")
        ch1=int(input("Enter your choice:"))
        
#TO UPDATE BOOK NAME        

        if ch1==1:
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)
            orderno=str(input("Enter order no:"))
            name_of_book=str(input("Enter new name:"))
            mycursor.execute("update buy_new_books set name_of_book='"+name_of_book+"' where orderno='"+orderno+"'")
            mydb.commit()
            print("*Name has been updated*")
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)
                
#TO UPDATE DELIVERY DATE
                
        if ch1==2:
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)
            orderno=str(input("Enter card no:"))
            del_date=str(input("Enter new delivery date(yyyy-mm-dd):"))
            mycursor.execute("update buy_new_books set del_date='"+del_date+"' where orderno='"+orderno+"'")
            mydb.commit()
            print("*Delivery date has been updated*")
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)
                
#TO UPDATE PRICE
                
        if ch1==3:
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)
            orderno=str(input("Enter card no:"))
            price=str(input("Enter new price:"))
            mycursor.execute("update buy_new_books set price='"+price+"' where orderno='"+orderno+"'")
            mydb.commit()
            print("*Price has been updated*")
            mycursor.execute("select * from buy_new_books")
            for i in mycursor:
                print(i)
          
        
#TO DISPLAY ORDERING HISTORY

    elif(ch==14):
        orderno=str(input("Enter order number:"))
        mycursor.execute("select * from buy_new_books where orderno='"+orderno+"'")
        for i in mycursor:
            print(i)
            
#TO EXIT THE PROGRAM
            
    else:
        break 