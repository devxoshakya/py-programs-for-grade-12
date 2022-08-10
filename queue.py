def peek(myQueue):
    if isEmpty(myQueue):
        print('Queue is empty')
        return None
    else:
        return myQueue[0]
    
def enqueue(myQueue, element):
    myQueue.append(element)

def isEmpty(myQueue):
    if len(myQueue)==0:
        return True
    else:
        return False

def dequeue(myQueue):
    if not (isEmpty(myQueue)):
        return myQueue.pop(0)
    else :
        print("Queue is empty")
def size(myQueue):
    return len(myQueue)


myQueue = list()
# each person to be assigned a code as P1, P2, P3,...
element = input("enter person’s code to enter in queue :")
enqueue(myQueue,element)
element = input("enter person’s code for insertion in queue :")
enqueue(myQueue,element)
print("person removed from queue is:", dequeue(myQueue))
print("Number of people in the queue is :",size(myQueue))
element = input("enter person’s code to enter in queue :")
enqueue(myQueue,element)
element = input("enter person’s code to enter in queue :")
enqueue(myQueue,element)
element = input("enter person’s code to enter in queue :")
enqueue(myQueue,element)
print("Now we are going to remove remaining people from the queue")
while not isEmpty(myQueue):
  print("person removed",dequeue(myQueue))























































































  #there is a hidden file in this same directory go find it
