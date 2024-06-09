import sys


def backtracking(depth, cnt, answer):
    if depth == c:
        if len(answer) == l and cnt >= 1 and len(answer) - cnt >= 2:
            print(''.join(answer))
        return

    backtracking(depth + 1, cnt + tbl[ord(arr[depth])], answer + arr[depth])
    backtracking(depth + 1, cnt, answer)


l, c = map(int, sys.stdin.readline().strip().split())
arr = list(sys.stdin.readline().strip().split())
arr.sort()
tbl = [0] * 128

for ch in ('a', 'e', 'i', 'o', 'u'):
    tbl[ord(ch)] = 1

# depth, 모음의 개수, 완성되는 문자열
backtracking(0, 0, '')
