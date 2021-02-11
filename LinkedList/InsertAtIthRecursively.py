class Node:
    def __init__(self, data) -> None:
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


def RecursiveInsert(head, curr, data)-> Node:
    if curr<0:
        return head
    if curr == 0:
        newNode = Node(data)
        newNode.next = head
        head = newNode
        return head
    newNode = RecursiveInsert(head.next, curr -1, data)
    head.next = newNode
    return head


    


head = takeInput()
printLL(head)
data = int(input("Enter data to be added\n"))
curr = int(input("Enter position to be added at\n"))
head = RecursiveInsert(head, curr, data)
printLL(head)
        
            

