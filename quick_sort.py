import sys
import math
import random

# sys.stdin = open("problemname.in", "r")
# sys.stdout = open("problemname.out", "w")

# Time Complexity - 
# Best case - O(n log n)
# Average case - O(n log n)
# Worst case - O(n * n)

# Space Complexity - O(log n)

def quicksort(a):
  if len(a) <= 1:
    return a
  pivot = random.randint(0, len(a))
  b = []
  c = []
  for i in range(len(a)):
    if i == pivot:
      continue
    if a[i] <= a[pivot]:
      b.append(a[i])
    else:
      c.append(a[i])
  sorted_b = quicksort(b)
  sorted_c = quicksort(c)
  sorted_a = []
  for x in sorted_b:
    sorted_a.append(x)
  sorted_a.append(a[pivot])
  for x in sorted_c:
    sorted_a.append(x)
  return sorted_a

if __name__ == '__main__':
  n = int(input())
  a = list(map(int, input().split()))
  ans = quicksort(a)
  for x in ans:
    print(x, end = " ")