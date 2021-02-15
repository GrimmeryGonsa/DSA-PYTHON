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



def NodePrinterAtAGivenDepth(root, k)->None:
    if root is None:
        return
    if k == 0:
        print(root.data)
        return
    NodePrinterAtAGivenDepth(root.left, k-1)
    NodePrinterAtAGivenDepth(root.right, k-1)

root = takeInput()
printTreeDetailed(root)
NodePrinterAtAGivenDepth(root,2)