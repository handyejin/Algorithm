import sys


def cal(a, b):
    s1 = cal2(a)
    s2 = cal2(b)

    return abs(s1 - s2)


def cal2(ls):
    s = 0
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i != j:
                s += arr[ls[i]][ls[j]]
    return s


def dfs(depth, start):
    global m
    if depth == n // 2:
        team1 = answer
        team2 = []
        for i in range(n):
            if i not in team1:
                team2.append(i)
        m = min(m, cal(team1, team2))
        return

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            dfs(depth + 1, i)
            del answer[-1]
            visited[i] = False


n = int(sys.stdin.readline().strip())

arr = []
visited = [False] * n
answer = []
m = 101

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

dfs(0, 0)
print(m)
