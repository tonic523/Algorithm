N, r, c = map(int, input().split())
def sol(N, r, c):
    if N == 0:
        return 0
    max = 2 ** N
    len = max // 2
    if r > len:
        if c > len:
            order = 3
            r -= len
            c -= len
        else:
            order = 2
            r -= len
    else:
        if c > len:
            order = 1
            c -= len
        else:
            order = 0
    result = (len ** 2) * order
    return result + sol(N-1, r, c)
print(sol(N,r+1,c+1))