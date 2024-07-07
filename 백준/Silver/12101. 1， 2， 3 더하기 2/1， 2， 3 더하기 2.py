import sys


def dfs(depth):
    global count, result
    if sum(answer) == n:
        s = '+'.join(str(x) for x in answer)
        if s not in answer_set:
            answer_set.add(s)
            if count == k:
                result = s
            count += 1
        return

    if depth == n:
        return

    for i in range(1, 4):
        answer.append(i)
        dfs(depth + 1)
        del answer[-1]


n, k = map(int, sys.stdin.readline().strip().split())
result = -1
answer_set = set()
count = 1
answer = []
dfs(0)
print(result)
