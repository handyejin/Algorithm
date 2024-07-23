import sys

n, m = map(int, sys.stdin.readline().strip().split())
hm = {}
result = list()

for i in range(n+m):
    ipt = sys.stdin.readline().strip()

    if ipt in hm:
        hm[ipt] = hm.get(ipt) + 1
    elif ipt not in hm:
        hm[ipt] = 1

for key, value in hm.items():
    if value > 1:
        result.append(key)

print(len(result))
result.sort()
for r in result:
    print(r)