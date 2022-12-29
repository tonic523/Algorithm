import sys

input = sys.stdin.readline

# 입력
S = input().rstrip()
quiz = []
quiz_character = set()
for _ in range(int(input())):
    c, i, j = input().rstrip().split()
    quiz.append([c, int(i), int(j)])
    quiz_character.add(c)

# 입력된 문자의 누적합 리스트 생성
c_prefix_sum = {}
for c in quiz_character: # 최대 26개
    temp = [0] * len(S)
    for i in range(len(S)): # 20만
        if c == S[i]:
            temp[i] = temp[i-1] + 1
        else:
            temp[i] = temp[i-1]
    c_prefix_sum[c] = temp

# 계산
answers = []
for q in quiz: # 최대 20만번
    prefix_sum = c_prefix_sum[q[0]]
    answer = prefix_sum[q[2]] - prefix_sum[q[1]]
    if S[q[1]] == q[0]:
        answer += 1
    answers.append(str(answer))

print("\n".join(answers))

## pypy로 했을 때 풀이 성공
