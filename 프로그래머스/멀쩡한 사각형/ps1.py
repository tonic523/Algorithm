import math

def solution(w, h):
    tilt = h / w
    g = math.gcd(w, h)
    r, c = 1, 1
    answer = 0
    now = (c * h) / w
    while r <= h and c <= w:
        if r == now:
            answer += 1
            answer *= g
            break
        if r < now:
            r += 1
        else:
            c += 1
            now = c * tilt
        answer += 1
    return w * h - answer

print(solution(3, 7))