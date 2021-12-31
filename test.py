import sys

T = int(input())

result=[]
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    result.append(A+B)
for i in result:
    print(i)