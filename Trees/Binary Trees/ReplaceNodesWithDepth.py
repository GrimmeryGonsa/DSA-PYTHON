#Replace Node With Depth
"""
Given a a binary tree. Replace each of it's data with the depth of tree.
Root is at depth 0, change its value to 0 and next level nodes are at depth 1 and so on.
Print the tree after modifying in inorder fashion.

Input format :
Line 1 :  Elements in level order form (separated by space)
(If any node does not have left or right child, take -1 in its place)

Output Format :
Inorder traversal of modified tree.
"""

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


def replaceDataWithDepth(root, depth)->None:
    if root == None:
        return
    root.data = depth
    replaceDataWithDepth(root.left, depth+1)
    replaceDataWithDepth(root.right, depth+1)


def Inorder(root):
    if root is None:
        return
    Inorder(root.left)
    print(root.data)
    Inorder(root.right)


root = takeInput()
printTreeDetailed(root)
replaceDataWithDepth(root)
printTreeDetailed(root)
Inorder(root)
