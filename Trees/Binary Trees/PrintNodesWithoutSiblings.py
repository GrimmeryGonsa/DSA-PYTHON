class BinaryTreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None

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

def nodeWithoutSiblings(root)->None:
    if root is None:
        return
    if root.left is not None and root.right is not None:
        nodeWithoutSiblings(root.left)
        nodeWithoutSiblings(root.right)
    elif root.right is not None:
        print(root.right.data)
        nodeWithoutSiblings(root.right)
    elif root.left is not None:
        print(root.left.data)
        nodeWithoutSiblings(root.left)


root = takeInput()
printTreeDetailed(root)
nodeWithoutSiblings(root)