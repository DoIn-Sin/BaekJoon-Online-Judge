import sys

input = sys.stdin.readline

N = int(input())
num_arr = []

for _ in range(N):
    X = int(input())
    num_arr.append(X)

num_arr = sorted(num_arr)

for num in num_arr:
    print(num)
