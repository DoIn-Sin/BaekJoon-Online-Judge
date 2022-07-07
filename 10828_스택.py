import sys

input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
    command = input().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "top":
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == "pop":
        if len(stack) >= 1:
            print(stack[-1])
            stack = stack[:-1]
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    else:
        if len(stack) >= 1:
            print(0)
        else:
            print(1)
