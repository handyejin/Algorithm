import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
Min = [sys.maxsize, 0, 0]

start = 0
end = n-1

while start < end:
    s = arr[start] + arr[end]

    if Min[0] >= abs(s):
        Min[0] = abs(s)
        Min[1] = start
        Min[2] = end

        if s==0:
            break

    if s < 0:
        start += 1
    else:
        end -= 1


print(f'{arr[Min[1]]} {arr[Min[2]]}')