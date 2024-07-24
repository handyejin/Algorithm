import sys

n = int(sys.stdin.readline().strip())
ipt = list(map(int, sys.stdin.readline().strip().split()))
arr = []

for i in range(n):
    arr.append([i, ipt[i]])

arr.sort(key=lambda x: x[1])

count = -1
check = 1000001

for i in range(n):
    if arr[i][1] != check:
        count += 1
        check = arr[i][1]
    arr[i][1] = count
arr.sort()

print(' '.join(str(x[1]) for x in arr))