class TreeNode:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
        
# Manual tree construction (explicit, good for learning)
#Inefficient
tree=TreeNode(2)
tree.left=TreeNode(3)
tree.right=TreeNode(5)
tree.left.left=TreeNode(1)
tree.right.left=TreeNode(3)
tree.right.right=TreeNode(7)
tree.right.left.right=TreeNode(4)
tree.right.right.right=TreeNode(8)
tree.right.right.left=TreeNode(6)

#Traversal

#1. Inorder
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.key)
    inorder(node.right)

#2. Preorder
def preorder(node):
    if node is None:
        return
    print(node.key)
    preorder(node.left)
    preorder(node.right)   

print("Inorder:")
inorder(tree)

print("Preorder:")
preorder(tree)
