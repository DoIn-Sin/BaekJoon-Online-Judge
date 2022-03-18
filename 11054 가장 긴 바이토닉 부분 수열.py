import sys

input = sys.stdin.readline

N = int(input())

numList = list(map(int, input().split()))
dp = [1 for _ in range(N)]

max_num = max(numList)

for i in range(1, N):
    for j in range(i):
        if numList[i] > numList[j]:
            dp[i] = max(dp[i], dp[j]+1)

for i in range(N-1):
    for j in range(i+1, N):
        if numList[i] > numList[j]:
            dp[j] = max(dp[j], dp[i]+1)
        
print(max(dp))