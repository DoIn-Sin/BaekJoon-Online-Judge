import sys
from collections import deque

input = sys.stdin.readline

def bfs(a, b):
	queue = deque([[a, b]])
	visited[a][b] = 1
	
	while queue:
		x, y = queue.popleft()
		
		if x==end_a and y==end_b:
			return visited[x][y]
		
		for i in range(8):
			nx = x+dx[i]
			ny = y+dy[i]
			
			if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
				visited[nx][ny] = visited[x][y]+1
				queue.append([nx, ny])

T = int(input())

for _ in range(T):
	N = int(input())
	start_a, start_b = map(int, input().split())
	end_a, end_b = map(int, input().split())
	
	visited = [[0]*N for _ in range(N)]
	
	dx = [2, 2, -2, -2, 1, 1, -1, -1]
	dy = [1, -1, 1, -1, 2, -2, 2, -2]
	
	print(bfs(start_a, start_b)-1)