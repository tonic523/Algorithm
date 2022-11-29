def solution(k, tangerine):
    answer = 0
    orange_by_count = {}
    for t in tangerine:
        if orange_by_count.get(t):
            orange_by_count[t] += 1
        else:
            orange_by_count[t] = 1

    order_by_count = sorted(orange_by_count.items(), key=lambda item:item[1], reverse=True)

    for o in order_by_count:
        orange, count = o
        if k <= 0:
            break
        k -= count
        answer += 1

    return answer
