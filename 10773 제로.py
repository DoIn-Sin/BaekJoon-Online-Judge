import sys

input = sys.stdin.readline

K = int(input())
total = []

for i in range(K):
    number = int(input())
 
    if number == 0:
        total.pop()
        continue
        
    total.append(number)

print(sum(total))
