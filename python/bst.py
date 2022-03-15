class Node:
  def __init__(self, val, parent, left=None, right=None):
    self.val = val
    self.parent = parent
    self.left = left
    self.right = right

class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.min = None
    self.max = None
  
  def insert(self, val):
    if not self.root:
      self.root = Node(val, None)
      self.min = self.root
      self.max = self.root
      return

    parent = self.root

    while True:
      if val < parent.val:
        if not parent.left:
          parent.left = Node(val, parent)

          if val < self.min.val:
            self.min = parent.left

          break

        parent = parent.left
      else:
        if not parent.right:
          parent.right = Node(val, parent)

          if val > self.max.val:
            self.max = parent.right

          break

        parent = parent.right

  def successor(self, node):
    if not node or node == self.maximum():
      return None
    
    if node.right:
      min = node.right
      while min.left:
        min = min.left
      return min
    
    if not node.parent:
      return None
    
    parent = node.parent

    while parent != None and parent.val < node.val:
      parent = parent.parent

    return parent

  def minimum(self):
    return self.min

  def maximum(self):
    return self.max

def print_tree(root):
  if root:
    print_tree(root.left)
    print(root.val, end=" ")
    print_tree(root.right)

def main():
  bst = BinarySearchTree()
  bst.insert(8)
  bst.insert(3)
  bst.insert(10)
  bst.insert(1)
  bst.insert(6)
  bst.insert(14)
  bst.insert(13)
  bst.insert(4)
  bst.insert(7)

  print_tree(bst.root)
  print()
  print()
  print(f"Min = {bst.min.val}")
  print(f"Max = {bst.max.val}")
  print()
  print("Print with successor():")

  curr = bst.min
  while curr != None:
    print(curr.val, end=" ")
    curr = bst.successor(curr)

if __name__ == "__main__":
  main()