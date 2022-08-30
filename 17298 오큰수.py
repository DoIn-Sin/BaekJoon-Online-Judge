import sys
input = sys.stdin.readline

N = int(input())
num_arr = list(map(int, input().split()))
stack = [0]
answer = [-1 for _ in range(N)]

for i in range(1, N):
	while stack and num_arr[stack[-1]] < num_arr[i]:
		answer[stack.pop()] = num_arr[i]
	stack.append(i)

print(*answer)
