import sys
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    
arr_sorted = sorted(arr)

for i in range(n):
    print(arr_sorted[i][0], arr_sorted[i][1])
