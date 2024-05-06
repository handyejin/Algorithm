import sys
import heapq

n = int(input())
max_length = n
heap = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    for x in arr:
        if len(heap) < max_length:
            heapq.heappush(heap, x)
        else:
            heapq.heappushpop(heap, x)

print(heapq.heappop(heap))