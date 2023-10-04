# 큐
import sys
# n = int(sys.stdin.readline())
n = int(input())

i = []
for _ in range(n):
    #a = sys.stdin.readline().split()
    a = input().split()
    o = a[0]

    if o =="push":
        i.append(int(a[1]))
    elif o == "pop":
        if len(i):
            