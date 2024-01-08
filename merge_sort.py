import sys
import math

# sys.stdin = open("problemname.in", "r")
# sys.stdout = open("problemname.out", "w")

# Time Complexity 
# Best Case - (n log n)
# Average Case - (n log n)
# Worst Case - (n log n)

# Space Complexity - O(n)

def mergesort(a):
  if len(a) <= 1:
    return a
  mid = len(a)//2
  b = a[:mid]
  c = a[mid:]
  sorted_b = mergesort(b)
  sorted_c = mergesort(c)
  sorted_a = []
  l = r = 0
  for i in range(len(a)):
    if l == len(sorted_b):
      sorted_a.append(sorted_c[r])
      r += 1
    elif r == len(sorted_c):
      sorted_a.append(sorted_b[l])
      l += 1
    elif sorted_b[l] < sorted_c[r]:
      sorted_a.append(sorted_b[l])
      l += 1
    else:
      sorted_a.append(sorted_c[r])
      r += 1
  return sorted_a


if __name__ == '__main__':
  n = int(input())
  a = list(map(int, input().split()))
  ans = mergesort(a)
  for x in ans:
    print(x, end = " ")