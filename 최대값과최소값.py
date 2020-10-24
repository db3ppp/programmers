#연습문제_level2??

def solution(s):
    answer = ''
    lst = s.split(' ')

    for i,element in enumerate(lst):
        lst[i] = int(element)
    mini = min(lst)
    maxi = max(lst)
    
    answer = str(mini)+' '+str(maxi)
    return answer
