import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append([nx, ny])

M, N = map(int, input().split())
day = 0

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [[False]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        day = max(j, day)
print(day-1)
