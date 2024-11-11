import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    words = list(sys.stdin.readline().strip().split())
    answer = ''

    for w in words:
        if not answer:
            answer = w
        else:
            if w <= answer[0]:
                answer = w + answer
            else:
                answer = answer + w
    print(answer)