def solution(numbers, target):
    answer = 0
    stack = []
    stack.append((numbers[0], 0))
    stack.append((-numbers[0], 0))
    while stack:
        now, i = stack.pop()
        if i == len(numbers)-1:
            if now == target:
                answer += 1
            continue

        stack.append((now + numbers[i+1], i+1))
        stack.append((now - numbers[i+1], i+1))
    return answer