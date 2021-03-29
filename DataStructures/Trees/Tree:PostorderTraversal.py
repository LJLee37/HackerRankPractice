class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    stack = []
    current = root
    popping = False
    leftVisited = []
    while not (popping and current == root and root not in leftVisited):
        if popping:
            if current in leftVisited:
                leftVisited.remove(current)
                current = current.right
                popping = False
                continue
            print(current.info, end=" ")
            stack.pop(-1)
            current = stack[-1]
        elif current.left != None:
            if current.right != None:
                leftVisited.append(current)
            stack.append(current)
            current = current.left
        elif current.right != None:
            stack.append(current)
            current = current.right
        else:
            popping = True
            stack.append(current)
    print(current.info)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)
