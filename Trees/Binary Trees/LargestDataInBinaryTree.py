import math
class BinaryTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def printTreeDetailed(root)->None :
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



def takeInput()->BinaryTreeNode:
    NodeData = int(input("enter the data or enter -1 to terminate\n"))
    if NodeData ==-1:
        return None
    root = BinaryTreeNode(NodeData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root


def getMaxElement(root):
    if root is None:
        return -math.inf
    return max(getMaxElement(root.left),getMaxElement(root.right),root.data)


root = takeInput()
printTreeDetailed(root)
print("largest element in tree:")
print(getMaxElement(root))
