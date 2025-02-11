import sys

n = int(sys.stdin.readline().strip())

l = list(map(int, sys.stdin.readline().strip().split()))
l.sort()

prefix_sum = [l[0]]

for i in range(1, n):
    prefix_sum.append(prefix_sum[i-1]+l[i])

print(sum(prefix_sum))