class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def takeInput()-> Node:
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None

    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        return head


def printLL(head) -> None:
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
    print('None')
    return

def length(head) -> int:
    count = 0
    while head is not None:
        count = count + 1
        head = head.next
    return count

def DeleteIthNode(head, pos) -> Node:
    if pos<0 and pos>= length(head):
        print("given position is outside the range of operation hence no changes are made")
        return head
    if pos == 0:
        head = head.next
        return head
    

    
    