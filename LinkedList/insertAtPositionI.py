class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def takeInput() -> Node:
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1 :
            break
        newNode = Node(currData)
        newNode.next = None
        if head is None:
            head = tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def printLL(head) -> None:
    while head is not None:
        print(str(head.data)+"->",end='')
        head = head.next
    print('None')
    return

def length(head) -> Node:
    count = 0
    while head is not None:
        count = count + 1
        head = head.next 
    return count
def insertAtIth(head, pos, data) -> Node:
    if pos<0 and pos> length(head) :
        return head
    count = 0
    prev = None
    curr = head

    while count < pos:
        prev = curr
        curr = curr.next
        count = count+1
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr

    return head



head = takeInput()
printLL(head)
data = int(input("Enter the data to be added\n"))
pos = int(input("Ener the position to be added at\n"))
head = insertAtIth(head, pos, data)
printLL(head)
        
            

