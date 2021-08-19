import sys

stack = []
for _ in range(int(input())):
    command = sys.stdin.readline().rstrip()
    if "push" in command:
        command, number = command.split()
        number = int(number)
        stack.append(number)
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(0 if stack else 1)
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)