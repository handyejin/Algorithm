import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
arr = []

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(k):
    y, x = map(int, sys.stdin.readline().strip().split())
    arr.append((x, y))

l = int(sys.stdin.readline().strip())
xc = dict()
for _ in range(l):
    x, c = sys.stdin.readline().strip().split()
    xc[int(x)] = c

# 머리 , 꼬리
now = [(0, 0)]

result = 0
d = 3

while True:
    if 0 <= now[0][0] < n and 0 <= now[0][1] < n and 0 <= now[-1][0] < n and 0 <= now[- 1][1] < n:
        result += 1
        is_apple = False
        nx = now[-1][0] + dx[d]
        ny = now[-1][1] + dy[d]
        if (nx, ny) in now:
            break
        now.append((nx, ny))
        for i in range(len(arr)):
            if arr[i][0] == nx + 1 and arr[i][1] == ny+1:
                del arr[i]
                is_apple = True
                break
        if not is_apple:
            now.pop(0)

        if result in xc:
            rc = xc[result]
            if rc == 'D':
                if d == 3:
                    d = 0
                else:
                    d += 1

            else:
                if d == 0:
                    d = 3
                else:
                    d -= 1

    else:
        break


print(result)
