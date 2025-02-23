from collections import deque
import sys
input = sys.stdin.readline


def BFS(start, group):
    que = deque([start])
    visited[start] = group

    while que:
        node = que.popleft()

        for link_node in graph[node]:
            if not visited[link_node]:
                que.append(link_node)
                visited[link_node] = -visited[node]
            elif visited[link_node] == visited[node]:
                return True

    return False


if __name__ == "__main__":
    K = int(input())

    for _ in range(K):
        V, E = map(int, input().split())

        graph = [[] for _ in range(V+1)]
        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (V+1)

        for i in range(1, V+1):
            if not visited[i]:
                result = BFS(i, 1)
                if result:
                    print("NO")
                    break
        else:
            print("YES")