import sys

arr = list(map(int, sys.stdin.readline().strip()))

count = {0: 0, 1: 0}
check_num = arr[0]

for idx in range(1, len(arr)):
    if arr[idx] == check_num:
        pass
    else:
        count[check_num] += 1
        check_num = arr[idx]

    if idx == len(arr) -1:
        if not (count[0] == 0 and count[1] == 0):
            count[check_num] += 1

print(min(count[0], count[1]))



