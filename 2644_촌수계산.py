import sys
sys.setrecursionlimit(100000)

def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = visited[v]+1
            dfs(i)

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a)

if visited[b]:
    print(visited[b])
else:
    print(-1)
