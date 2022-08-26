import sys

def virus(key):
    result = 0
    v_computers = computers[key]
    for idx, v_computer in enumerate(v_computers):
        if idx == 0:
            if v_computer == 1:
                return -1
            else:
                computers[key][0] = 1
        else:
            result += virus(v_computer) + 1
    return result

computer = int(input())
computers = [[0] for _ in range(101)]
for _ in range(int(input())):
    key, value = map(int, sys.stdin.readline().rstrip().split())
    computers[key].append(value)
    computers[value].append(key)
print(virus(1))