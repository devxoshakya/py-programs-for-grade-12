5] Write a program to count a total number of lines and count the total number of lines starting with ‘A’, ‘B’, and ‘C’. (Consider the merge.txt file)

def program5():
    with open("merge.txt","r") as f1:
       data=f1.readlines()
    cnt_lines=0
    cnt_A=0
    cnt_B=0
    cnt_C=0
    for lines in data:
        cnt_lines+=1
        if lines[0]=='A':
            cnt_A+=1
        if lines[0]=='B':
            cnt_B+=1
        if lines[0]=='C':
            cnt_C+=1
    print("Total Number of lines are:",cnt_lines)
    print("Total Number of lines strating with A are:",cnt_A)
    print("Total Number of lines strating with B are:",cnt_B)
    print("Total Number of lines strating with C are:",cnt_C)
program5()
[6] Find the total occurrences of a specific word from a text file:

def program6():
    cnt = 0
    word_search = input("Enter the words to search:")
    with open("merge.txt","r") as f1:
        for data in f1:
            words = data.split()
            for word in words:
                if (word == word_search):
                    cnt+=1
    print(word_search, "found ", cnt, " times from the file")
program6()
Python File Handling Programs based on read(), readline() and readlines() functions.

[7] Read first n no. letters from a text file, read the first line, read a specific line from a text file.

def program7():
    cnt = 0
    n = int(input("Enter no. characters to read:"))
    with open("merge.txt","r") as f1:
       line1=f1.readline()
       print("The first line of file:",line1)
       nchar=f1.read(n)
       print("First n no. of characters:", nchar)
       nline=f1.readlines()
       print("Line n:",nline[n])
program7()
Python File Handling Programs based on replace contents.

[8] Replace all spaces from text with – (dash).

def program8():
    cnt = 0
    n = int(input("Enter no. characters to read:"))
    with open("merge.txt","r") as f1:
       data = f1.read()
       data=data.replace(' ','-')
    with open("merge.txt","w") as f1:
        f1.write(data)
program8()
Python File Handling Programs based on tell() and seek() functions.

[9] Write a program to know the cursor position and print the text according to below-given specifications:

Print the initial position
Move the cursor to 4th position
Display next 5 characters
Move the cursor to the next 10 characters
Print the current cursor position
Print next 10 characters from the current cursor position
def program9():
    f = open("merge.txt","r")
    print(f.tell())
    f.seek(4,0)
    print(f.read(5))
    f.seek(10,0)
    print(f.tell())
    print(f.seek(7,0))
    print(f.read(10))
program9()
Python File Handling Programs based on high order thinking skills.

[10] Append the contents in entered by the user in the text file:

def program10():
    text = input("Enter text to append in the file:")
    with open("merge.txt","a") as f1:
        f1.write(text)
program10()
Read the assignments

[11] Read the contents of file in reverse order:

def program11():
    for i in reversed(list(open("merge.txt","r"))):
        print(i.rstrip())
program11()
[12] Replace multiple spaces with single space in a text file.

def program12():
    f1 = open("merge.txt","rt")
    f2 = open("merge1.txt","wt")
    for line in f1:
        f2.write(' '.join(line.split()))
    f1.close()
    f2.close()
program12()
Method 2:

import re
def program12():
    f1 = open("merge.txt","rt")
    f2 = open("merge3.txt","wt")
    for line in f1:
        f2.write(re.sub('\s+',' ',line))
    f1.close()
    f2.close()
program12()
Thank you very much for reading Python File Handling Programs.

