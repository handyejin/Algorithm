import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

ipt = list(map(int, sys.stdin.readline().strip().split()))
ipt.sort()

distance = []

for i in range(1, len(ipt)):
    distance.append(ipt[i] - ipt[i-1])


distance.sort(reverse=True)
print(sum(distance[m-1:]))