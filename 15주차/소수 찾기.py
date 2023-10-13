from itertools import permutations
prime = set()
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    temp = []
    for i in range(1, len(numbers)+1):
        temp += (list(permutations(numbers, i)))
    num = [int(''.join(t)) for t in temp]
    for i in num:
        if is_prime(i):
            prime.add(i)
    answer = len(prime)
    return answer