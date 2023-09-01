import math

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
        	return False
    return True

def solution(n, k):
    answer = 0
    tmp = ''
    while n:
        tmp += str(n % k)
        n = n // k
    n_decimal = tmp[::-1]
    primes = n_decimal.split('0')
    for prime in primes:
        if prime and is_prime(int(prime)):
            answer += 1
    return answer