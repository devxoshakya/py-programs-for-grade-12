# ANSWERKEY SET - B



(A) PYTHON PROGRAM 


vowels = ["a" ,"e" ,"i" ,"o" ,"u"]

consonants = ["b" ,"c" ,"d" ,"f" ,"g" ,"h" ,"j",             "k", "l", "m", "n", "p", "q", "r", 
              "s", "t", "v", "w", "x", "y", "z"]

with open("sample.txt", "r") as file:
    
    # Read File
    data = file.read()

    # Initialize counter
    count_c = 0
    count_v = 0
    count_upper = 0
    count_lower = 0
    
    # Loop through Text
    for c in data:
        if (c.islower()):
            count_lower +=1
        elif(c.isupper()):
            count_upper +=1
        c = c.lower()
        if c in vowels:
            count_v += 1
        elif c in consonants:
            count_c += 1

    print("Number of Consonants:",count_c)
    print("Number of vowels:",count_v)
    print("Number of Lowercase:",count_lower)
    print("Number of Uppercase:",count_upper)
    
    
    '''
    OUTPUT —
    
      Number of vowels: 20
      Number of consonants: 29
      Number of Uppercase : 3  
      Number of Lowercase : 46
      
    '''
    
    
    
    
(B) MySql Stuble Program 



Statement 1: mqsql.connector

Statement 2: con1.cursor()

Statement 3: mycursor.execute("select * from student where Marks>75")

Statement 4: mycursor.fetchall()

