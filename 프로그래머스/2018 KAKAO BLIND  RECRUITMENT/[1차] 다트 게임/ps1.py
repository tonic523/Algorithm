'''
S(1), D(2), T(3) 가 나오면 캐시에 결과값을 저장한다.
- 이전에 있던 숫자들은 결과에 더한다.

- *은 다른 옵션들과 중첩이 될 수 있다.
- 옵션 *은 2배, # 은 -
'''

def solution(dartResult):
    answer = 0
    cache = []

    point = [str(i) for i in range(0, 11)]
    bonus = {'S':1, 'D':2, 'T':3}
    option = ('*', '#')

    now_point = 0
    for dart in dartResult:
        if dart in point:
            if dart == '0' and now_point == 1:
                now_point = 10
            else:
                now_point = int(dart)
        elif dart in bonus.keys():
            now_point **= bonus[dart]
            cache.append(now_point)
        elif dart in option:
            if dart == '*':
                lastCache = cache.pop()
                if cache:
                    cache.append(cache.pop() * 2)
                cache.append(lastCache * 2)
            else:
                cache[len(cache)-1] *= -1
        print(cache)

    if cache:
        answer += sum(cache)

    return answer