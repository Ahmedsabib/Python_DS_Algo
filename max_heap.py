import sys
import math

from queue import *
from collections import *

# sys.stdin = open("problemname.in", "r")
# sys.stdout = open("problemname.out", "w")

def heapify(arr, n, i):
  largest = i
  left_child = 2 * i + 1
  right_child = 2 * i + 2

  if left_child < n and arr[i] < arr[left_child]:
    largest = left_child

  if right_child < n and arr[i] < arr[right_child]:
    largest = right_child

  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)


def insert(arr, new_num):
  size = len(arr)
  if size == 0:
    arr.append(new_num)
  else:
    arr.append(new_num)
    for i in range((size//2) - 1, -1, -1):
      heapify(arr, size, i)


def deleteNode(arr, num):
  size = len(arr)
  i = 0
  for i in range(0, size):
    if num == arr[i]:
      break

  arr[i], arr[size - 1] = arr[size - 1], arr[i]
  arr.remove(num)

  for i in range(len(arr)//2 - 1, -1, -1):
    heapify(arr, len(arr), i)


if __name__ == '__main__':
  arr = []
  insert(arr, 3)
  insert(arr, 4)
  insert(arr, 9)
  insert(arr, 5)
  insert(arr, 2)

  print("Max-Heap array: " + str(arr))
  deleteNode(arr, 4)
  print("After deleting an element: " + str(arr))