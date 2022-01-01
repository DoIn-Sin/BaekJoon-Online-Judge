N, K = map(int, input().split())

cnt = 0
money = []

for i in range(N):
    num = int(input())
    money.append(num)
    
for m in reversed(money):
    if K >= m :
        cnt += int(K/m)
        K = K%m
print(cnt)