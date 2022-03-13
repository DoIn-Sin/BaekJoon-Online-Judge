import sys
from collections import deque

input = sys.stdin.readline

def bfs(a, b):
    queue = deque([[a, b]])
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<M and 0<=ny<N:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0]*N for _ in range(M)]
    visited = [[0]*N for _ in range(M)]
    count = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                count += 1
    print(count)