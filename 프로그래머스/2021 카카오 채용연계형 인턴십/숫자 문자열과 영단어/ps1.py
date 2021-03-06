def solution(s):
    answer = ""
    eng_num = {
        "zero" : '0',
        "one" : '1',
        "two" : '2',
        "three" : '3',
        "four" : '4',
        "five" : '5',
        "six" : '6',
        "seven" : '7',
        "eight" : '8',
        "nine" : '9'
    }
    num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    temp = ""
    for c in s:
        if eng_num.get(temp+c):
            answer += eng_num[temp+c]
            temp = ""
        else:
            if c.isdigit():
                answer += c
            else:
                temp += c
    return int(answer)