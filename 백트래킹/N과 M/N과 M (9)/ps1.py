import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

numbers = sorted(list(map(int, input().rstrip().split())))
results = set()
def solve(sequence, numbers):
    # 모든 개수를 골랐을 때
    if len(sequence) == M:
        result = " ".join(map(str, sequence))
        # 중복된 순열이 아닐 때 출력
        if result not in results:
            results.add(result)
            print(result)
    # 모든 순열 조회
    for n in numbers:
        temp_sequence = list(sequence)
        temp_sequence.append(n)
        temp = list(numbers)
        temp.remove(n)
        solve(temp_sequence, temp)

solve([], numbers)