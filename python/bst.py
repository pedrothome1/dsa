class Node:
  def __init__(self, val, parent, left=None, right=None):
    self.val = val
    self.parent = parent
    self.left = left
    self.right = right
    self.leftn = 0
    self.rightn = 0


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
        parent.leftn += 1

        if not parent.left:
          parent.left = Node(val, parent)

          if val < self.min.val:
            self.min = parent.left

          break

        parent = parent.left
      else:
        parent.rightn += 1

        if not parent.right:
          parent.right = Node(val, parent)

          if val > self.max.val:
            self.max = parent.right

          break

        parent = parent.right

  def predecessor(self, node):
    if not node or node == self.minimum():
      return None

    if node.left:
      max = node.left
      while max.right:
        max = max.right
      return max

    if not node.parent:
      return None

    parent = node.parent

    while parent != None and parent.val > node.val:
      parent = parent.parent

    return parent

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

  def size(self):
    return self.root.leftn + self.root.rightn + 1

  #           R
  # 1 3 4 6 7 8 10 13 14
  def median(self):
    if self.root.leftn == self.root.rightn:
      return self.root.val

    size = self.size()
    root_idx = self.root.leftn
    mid = int((size-1)/2)
    idx = root_idx
    curr = self.root

    iterate = self.successor if idx < mid else self.predecessor
    off = 1 if idx < mid else -1

    while idx != mid:
      curr = iterate(curr)
      idx += off

    if size % 2 == 1:
      return curr.val

    m1 = curr.val
    m2 = self.successor(curr).val

    return (m1+m2)/2

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
  bst.insert(9)
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
  print(f"Min = {bst.minimum().val}")
  print(f"Max = {bst.maximum().val}")
  print()
  print("Print with successor():")

  curr = bst.minimum()
  while curr != None:
    print(f"{curr.val}", end=" ")
    curr = bst.successor(curr)

  print()
  print("Print with predecessor():")

  curr = bst.maximum()
  while curr != None:
    print(f"{curr.val}", end=" ")
    curr = bst.predecessor(curr)

  print()
  print(f"Median {bst.median()}")


if __name__ == "__main__":
  main()
