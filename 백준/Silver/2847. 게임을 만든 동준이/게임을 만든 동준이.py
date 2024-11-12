import sys

T = int(sys.stdin.readline().strip())
arr = []

for _ in range(T):
    arr.append(int(sys.stdin.readline().strip()))

Max = arr[-1]

answer = 0

for i in range(T-2, -1, -1):
    if Max <= arr[i]:
        Max = Max - 1
        answer += arr[i] - Max
    else:
        Max = arr[i]
print(answer)