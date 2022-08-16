def insertion_Sort(list3):
    n= len(list3)
    for i in range(n): # Traverse through all elements
        temp = list3[i]
        j = i-1
        while j >=0 and temp< list3[j] :
                list3[j+1] = list3[j]
                j = j-1
                list3[j+1] = temp
numList = []
k = int(input("Enter number of elements to add :"))
for i in range (0,k):
     n = int(input("Input element :"))
     numList.append(n)
insertion_Sort(numList)
print ('The sorted list is :')
for i in range(len(numList)):
    print (numList[i], end=" ")