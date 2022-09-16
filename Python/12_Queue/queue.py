# we can implement queue with the help of the list
# queue=list()
# Since Queue Follow LIFO order 
# insert element in the list using Append Method ,ALSO THIS METHOD IS KNOW AS ENQUEUE
# queue.append(10)
# queue.append(20)
# queue.append(30)
# Now for removing from the queue we have tio0 use POP method and specify the Zero Index 
# As Queue Follows Last in First Out Method 
# THIS METHOD IS KNOW AS DEQUEUE
# queue.pop(0)
# queue.pop(0)
# queue.pop(0)
queue=list()
def enqueue():
        element=input('Enter the element')
        queue.append(element)
        print(queue)

def dequeue():
    if not queue:
        print("Queue is emplty")
    else:
        removed_element=queue.pop(0)
        print(f"Removed Element:{removed_element}")
        print(queue)

def display():
    print(queue)

run=True

while run:
    print("Select the operation 1.Enqueue 2.Dequeue 3.Show4.Quit .")
    choice=int(input("Enter Your Choice."))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        run=False
    else:
        print("Enter the Correct option")

