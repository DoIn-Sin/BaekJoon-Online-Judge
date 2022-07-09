import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    stack = []

    command = input()

    for cmd in command:
        if cmd == "(":
            stack.append("(")
        elif cmd == ")":
            if len(stack) >= 1:
                if stack[-1] == "(":
                    stack = stack[:-1]
            else:
                stack.append(")")

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
