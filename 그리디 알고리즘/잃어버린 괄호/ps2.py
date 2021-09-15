import sys

input = sys.stdin.readline

def sol1541_2():
    line = input().rstrip().split('-')
    result = 0
    for i in line[0].split('+'):
        result += int(i)

    for i in line[1:]:
        for j in i.split('+'):
            result -= int(j)
    print(result)


if __name__ == "__main__":
    sol1541_2()