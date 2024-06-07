import sys


def is_valid_answer(answer):
    vowel_count = 0
    consonant_count = 0

    for s in answer:
        if s in ('a', 'e', 'o', 'u', 'i'):
            vowel_count += 1
        else:
            consonant_count += 1
    if vowel_count >= 1 and consonant_count >= 2:
        return True
    else:
        return False


def backtracking(depth, start):
    if depth == l:
        answer.sort()
        s = ''.join(answer)
        if s not in result:
            if is_valid_answer(s):
                result.add(s)
                print(s)
        return

    for i in range(start, c):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            backtracking(depth + 1, i)
            del answer[-1]
            visited[i] = False


l, c = map(int, sys.stdin.readline().strip().split())
arr = list(sys.stdin.readline().strip().split())
visited = [False] * c
answer = []
result = set()

arr.sort()

backtracking(0, 0)
