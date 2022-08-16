
def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
           
            if array[j] < array[min_index]:
                min_index = j
         
        (array[ind], array[min_index]) = (array[min_index], array[ind])

numList = []
k = int(input("Enter number of elements to add :"))
for i in range (0,k):
     n = int(input("Input element :"))
     numList.append(n)


size = len(numList)
selectionSort(numList, size)
print(numList)
