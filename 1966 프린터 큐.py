import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    
    while queue:
        max_num = max(queue)
        pop_num = queue.popleft()
        M -= 1
        
        if pop_num == max_num:
            count += 1
            if M < 0:
                print(count)
                break
        else:
            if M < 0:
                M = len(queue)
            queue.append(pop_num)
