
def selection_Sort(list2):
        flag = 0 #to decide when to swap
        n=len(list2)
        for i in range(n): # Traverse through all list elements
          min = i
          for j in range(i + 1, len(list2)): #the left elements
    #are already sorted in previous passes
             if list2[j] < list2[min]: # element at j is smaller
    #than the current min element
                 min = j
                 flag = 1
        if flag == 1 : # next smallest element is found
             list2[min], list2[i] = list2[i], list2[min]
numList = []

def main():
    k = int(input("Enter number of elements to add :"))
    for i in range (0,k):
        n = int(input("Input element :"))
        numList.append(n)




main()
selection_Sort(numList)
for i in range(len(numList)):
    print (numList[i], end=" ")