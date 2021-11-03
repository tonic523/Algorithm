def solve(s, size):
    start = 0
    end = size
    now = s[start:end]
    n_s = ""
    cnt = 1
    while end < len(s):
        start += size
        end += size
        next = s[start:end]
        if now == next:
            cnt += 1
        else:
            if cnt != 1:
                n_s += str(cnt)
                cnt = 1
            n_s += now
            now = next
    if cnt != 1:
        n_s += str(cnt)
    n_s += now
    return len(n_s)


def solution(s):
    answer = 1000
    if len(s) == 1:
        return len(s)
    for i in range(1, (len(s) // 2) + 1):
        answer = min(answer, solve(s, i))
    return answer