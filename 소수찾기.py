#완전탐색_level2

from itertools import permutations

def primeCheck(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
        
def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        permu = list(map(''.join, permutations(numbers, i)))
        for j in permu:
            if primeCheck(int(j)):
                answer.append(int(j))
                
    answer = len(set(answer)) #set으로 중복검사
    return answer
