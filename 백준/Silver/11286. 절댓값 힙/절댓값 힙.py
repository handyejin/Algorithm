import heapq
import sys

n = int(input())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))