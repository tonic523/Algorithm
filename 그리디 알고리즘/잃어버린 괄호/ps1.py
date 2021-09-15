import sys

input = sys.stdin.readline

def sol1541():
    line = input().rstrip().split('-')
    int_line = []
    for l in line:
        int_line.append(sum(map(int, l.split('+'))))

    result = int_line[0]
    for i in range(1, len(line)):
        result -= int_line[i]
    print(result)

if __name__ == "__main__":
    sol1541()