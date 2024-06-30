import sys
import heapq

n = int(sys.stdin.readline().strip())
hq = []
count = 0

dasom = int(sys.stdin.readline().strip())

for i in range(n-1):
    num = int(sys.stdin.readline().strip())
    heapq.heappush(hq, (-num, num))

if len(hq) == 0:
    print(count)

while len(hq) > 0:
    Max = heapq.heappop(hq)
    if Max[1] < dasom:
        print(count)
        break
    else:
        r_num = Max[1]-1
        heapq.heappush(hq, (-r_num, r_num))
        dasom += 1
        count += 1