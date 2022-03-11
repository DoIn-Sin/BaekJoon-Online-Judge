import sys
from collections import deque
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
count = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
def dfs(start):
    visited[start] = 1
    for idx, val in enumerate(graph[start]):
        if visited[idx] == 0 and val == 1:
            dfs(idx)
            
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)