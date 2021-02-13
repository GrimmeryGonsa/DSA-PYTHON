## Either 0,1 or 2 children, never contains cycles


class BinaryTreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None

def printTree(root)-> None:
    if root is None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)
    return

def printTreeDetailed(root) -> None:
    if root is None:
        return
    print(root.data,end = ':')
    if root.left is not None:
        print(' L ', root.left.data, end ='')
    if root.right is not None:
        print(' R ',root.right.data, end = '')
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


def takeInput():
    rootData = int(input("Enter element....enter -1 to terminate\n"))
    if rootData == -1 :
        return  None
    
    root = BinaryTreeNode(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def numberOfNodes(root)->int:
    if root is None:
        return 0
    return numberOfNodes(root.left) + numberOfNodes(root.right) +1



root = takeInput()
printTree(root)
print("Detailed:")
printTreeDetailed(root)
print("totaal number of nodes....")
print(numberOfNodes(root))