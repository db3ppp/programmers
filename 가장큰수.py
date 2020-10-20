#정렬_level2
'''
from itertools import permutations

permu = list(permutations(numbers, len(numbers)))
permList = [''.join(map(str, i)) for i in permu]
print(max(permList))
#permutation으로 하면 시간초과ㅠ 결국 다른 사람 풀이 참고했는데 lambda 어렵따,,
'''

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    answer = ''.join(numbers) #string element list => string
    return int(answer) #int로 안바꿔주면 [0,0,0,0,0,0] 이렇게 있을 때 "0" 하나만 나와야 하는 케이스에 걸린다..


