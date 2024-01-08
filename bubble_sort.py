import sys
import math

# sys.stdin = open("problemname.in", "r")
# sys.stdout = open("problemname.out", "w")

# Time Complexity - 
# Best case - O(n)
# Average case - O(n * n)
# Worst case - O(n * n)

# Space Complexity - O(1)

def quicksort(a):
  for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
      if a[j] > a[j + 1]:
        a[j], a[j + 1] = a[j + 1], a[j]
  return a

if __name__ == '__main__':
  n = int(input())
  a = list(map(int, input().split()))
  ans = quicksort(a)
  for x in ans:
    print(x, end = " ")