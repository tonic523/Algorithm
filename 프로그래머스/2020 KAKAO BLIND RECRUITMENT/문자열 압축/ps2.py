import sys

input = sys.stdin.readline


def solve(s, size):
    words = [s[i:i+size] for i in range(0, len(s), size)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(s):
    return min([solve(s, i) for i in range(1, (len(s) // 2)+1)] + [len(s)])

print(solution("c"))
