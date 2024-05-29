import sys

S = int(sys.stdin.readline().strip())

N = 0
s = 0
num = 1

while True:

    if s == S:
        print(N)
        break
    elif s > S:
        print(N-1)
        break
    else:
        N += 1
        s += N

