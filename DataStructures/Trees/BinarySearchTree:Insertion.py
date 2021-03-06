class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        prev = None
        cur = self.root
        newNode = Node(val)
        newNode.level = 0
        if cur == None:
            self.root = newNode
            return
        while cur != None:
            prev = cur
            newNode.level += 1
            if val > cur.info:
                cur = cur.right
            else:
                cur = cur.left
        if val > prev.info:
            prev.right = newNode
        else:
            prev.left = newNode

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)

