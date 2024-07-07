import sys
import math
# sys.setrecursionlimit(10**6)


def is_unique_prime(num):
    ch = ''
    for n in num:
        ch += n
        if int(ch) == 1:
            return False
        for i in range(2, int(math.sqrt(int(ch))) + 1):
            if int(ch) % i == 0:
                return False
    return True


def dfs(depth):
    global answer
    if depth == n:
        #if answer not in result_set:
            #result_set.add(answer)
        if is_unique_prime(answer):
            print(answer)
        return
    for i in (1, 2, 3, 5, 7, 9):
        answer += str(i)
        dfs(depth+1)
        answer = answer[0:-1]


n = int(sys.stdin.readline().strip())
answer = ''
# result_set = set()

dfs(0)
