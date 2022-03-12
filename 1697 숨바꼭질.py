import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

def bfs(N):
    queue = deque([N])
    visited = [0] * 100001
    
    while queue:
        start = queue.popleft()
        
        if start == K:
            print(visited[start])
            break
            
        for num in (start-1, start+1, 2*start):
            if 0<=num<=100000 and visited[num]==0:
                visited[num] = visited[start]+1
                queue.append(num)
bfs(N)