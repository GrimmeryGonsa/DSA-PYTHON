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

def LeafNodeCount(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return LeafNodeCount(root.left)+LeafNodeCount(root.right)

