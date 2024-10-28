import sys

x, y = map(float, sys.stdin.readline().strip().split())
z = y * 100 // x

start = 1
end = 1000000000
answer = -1
while start <= end:
    mid = (start+end)//2
    if (y + mid) * 100 // (x + mid) > z:
        end = mid-1
        answer = mid
    else:
        start = mid+1
print(answer)