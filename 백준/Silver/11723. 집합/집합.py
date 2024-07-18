import sys

n = int(sys.stdin.readline().strip())
S = set()
for _ in range(n):
    cal, *x = sys.stdin.readline().strip().split()
    if x:
        x = int(x[0])

    if cal == 'add':
        S.add(x)
    elif cal == 'remove':
        if x in S:
            S.discard(x)
    elif cal == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif cal == 'toggle':
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif cal == 'all':
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif cal == 'empty':
        S = set()
