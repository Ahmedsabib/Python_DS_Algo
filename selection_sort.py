import sys
import math

# sys.stdin = open("problemname.in", "r")
# sys.stdout = open("problemname.out", "w")

# Time Complexity - 
# Best case - O(n * n)
# Average case - O(n * n)
# Worst case - O(n * n)

# Space Complexity - O(1)

def quicksort(a):
  for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
      if a[j] < a[i]:
        a[j], a[i] = a[i], a[j]
  return a

if __name__ == '__main__':
  n = int(input())
  a = list(map(int, input().split()))
  ans = quicksort(a)
  for x in ans:
    print(x, end = " ")