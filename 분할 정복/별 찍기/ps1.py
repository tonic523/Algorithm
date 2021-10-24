import sys

input = sys.stdin.readline

N = int(input())
star = [
        "n*n",
        "n* *n",
        "n*****n"
    ]
for i in range(N):
    time = ((N - i - 1) // 3)
    if i % 3 == 0 and i != 0:
        for j in range(len(star)):
            star.append(star[j] + " " + star[j])
    for s in star[i]:
        if s == "n":
            print(" " * (N-i-1), end="")
        else:
            print(s, end="")
    print()