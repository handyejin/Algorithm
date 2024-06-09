import sys


def calculator(operator):
    s = n_arr[0]

    for i in range(n - 1):
        if operator[i] == 0:
            s = s + n_arr[i + 1]
        elif operator[i] == 1:
            s = s - n_arr[i + 1]
        elif operator[i] == 2:
            s = s * n_arr[i + 1]
        elif operator[i] == 3:
            s = int(s / n_arr[i + 1])
    return s


def backtracking(depth, answer):
    global visited, max_num, min_num
    if depth == n - 1:
        s = calculator(answer)
        if s > max_num:
            max_num = s
        if s < min_num:
            min_num = s
        return

    for idx in range(0, n - 1):
        if not visited[idx]:
            visited[idx] = True
            answer.append(p_operator[idx])
            backtracking(depth + 1, answer)
            visited[idx] = False
            del answer[-1]


n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().strip().split()))
operator = list(map(int, sys.stdin.readline().strip().split()))

p_operator = []
for i in range(4):
    opt = [i] * operator[i]
    p_operator.extend(opt)

visited = [False] * (n - 1)

min_num, max_num = 1000000000, -1000000000

backtracking(0, [])
print(max_num)
print(min_num)
