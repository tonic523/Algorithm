def is_prime_number(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True

M,N = map(int, input().split())

for number in range(M,N+1):
    if is_prime_number(number):
        print(number)