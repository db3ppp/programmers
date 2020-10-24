#연습문제_level2

'''
#recursion 시간초과
def fibonacci(n):
    if n < 3:
        fibo = 1
    else:
        fibo = fibonacci(n-2)+fibonacci(n-1)
    return fibo

def solution(n):
    answer = 0
    fibo = fibonacci(n) % 1234567
    return fibo
'''

def solution(n):
    answer = 0
    a = 0
    b = 1
    for i in range(n):
        sum = a+b
        a = b
        b = sum
        
    answer = a % 1234567
    return answer
