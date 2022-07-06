import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if 0<=nx<H and 0<=ny<N and 0<=nz<M and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z]+1
                queue.append([nx, ny, nz])

M, N, H = map(int, input().split())
day = 0

graph = []

queue = deque([])

for i in range(H):
    line = []
    for j in range(N):
        line.append(list(map(int, input().split())))
        for k in range(M):
            if line[j][k] == 1:
                queue.append([i, j, k])
    graph.append(line)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

bfs()

for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
            day = max(k, day)
print(day-1)
