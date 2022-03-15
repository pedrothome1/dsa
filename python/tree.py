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

# O(2n) Two-pass algorithm
def levelOrder(root):
    levels = {}
    
    # O(n) Group nodes by level and return last level
    def saveLevels(root, level):
        if root:
            if level in levels:
                levels[level].append(root)
            else:
                levels[level] = [root]
            
            if not root.left and not root.right:
                return level
            if not root.left:
                return saveLevels(root.right, level+1)
            if not root.right:
                return saveLevels(root.left, level+1)
            
            return max(saveLevels(root.left, level+1), saveLevels(root.right, level+1))
        return level-1
    
    lastLevel = saveLevels(root, 0)
    idx = 0
    
    # O(n)
    while idx <= lastLevel:
        for node in levels[idx]:
            print(node.info, end=" ")
        idx += 1

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
