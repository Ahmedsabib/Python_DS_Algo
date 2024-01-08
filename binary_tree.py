import sys
import math

# sys.stdin = open("problemname.in", "r")
# sys.stdout = open("problemname.out", "w")

# Binary Tree in Python

class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key


  # Traverse preorder
  def traversePreorder(self):
    print(self.val, end = '')
    if self.left:
      self.left.traversePreorder()
    if self.right:
      self.right.traversePreorder()


  # Traverse inorder
  def traverseInorder(self):
    if self.left:
      self.left.traverseInorder()
    print(self.val, end = '')
    if self.right:
      self.right.traverseInorder()


  # Traverse postorder
  def traversePostorder(self):
    if self.left:
      self.left.traversePostorder()
    if self.right:
      self.right.traversePostorder()
    print(self.val, end = '')


if __name__ == '__main__':
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)

  root.left.left = Node(4)

  print("Preorder traversal: ", end = '')
  root.traversePreorder()
  print("\nInorder traversal: ", end = '')
  root.traverseInorder()
  print("\nPostorder traversal: ", end = '')
  root.traversePostorder()