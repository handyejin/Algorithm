import sys

n = int(sys.stdin.readline().strip())

ls = [0] * (n+1)

ls[1] = 1
if n > 1:
    ls[2] = 2

if n in (1, 2):
    print(ls[n])

else:
    for i in range(3, n+1):

        ls[i] = ls[i-1] + ls[i-2]

    print(ls[n] % 10007)

