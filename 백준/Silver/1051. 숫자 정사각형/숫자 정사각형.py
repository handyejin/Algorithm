import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = []
lv = 0
result = 1
status = True
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))

while lv < min(m, n):
    status = False
    for i in range(n-lv):
        for j in range(m-lv):
            if arr[i][j] == arr[i+lv][j] == arr[i][j+lv] == arr[i+lv][j+lv]:
                result = lv
                status = True
                break
        if status:
            break
    lv += 1
    
print((result+1)**2)