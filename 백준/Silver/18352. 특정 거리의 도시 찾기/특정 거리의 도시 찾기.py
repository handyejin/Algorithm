import sys
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if dist > dis[node]:
            continue

        for n in graph[node]:
            new_cost = dist + 1

            if new_cost < dis[n]:
                dis[n] = new_cost
                heapq.heappush(q, (new_cost, n))


INF = 1e8
N, M, K, X = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N + 1)]
dis = [INF] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)

dijkstra(X)

answer = []
for i in range(1, N+1):
    if dis[i] == K:
        answer.append(i)

if answer:
    for i in answer:
        print(i)
else:
    print(-1)