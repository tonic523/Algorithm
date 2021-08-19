def is_prime_number(number):
    if number == 1:
        return 0
    if number == 2:
        return 1
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return 0
    return 1

N = int(input())
arr = map(int, input().split())
result = 0
for number in arr:
    if is_prime_number(number):
        result += 1
print(result)