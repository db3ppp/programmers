#greedy_level2

def solution(people, limit):
    answer = 0
    people.sort()
    i=0 #min
    j=len(people)-1 #max
    
    while i < j:
        if people[i] + people[j] <= limit:
            answer += 1
            i += 1
            j -=1
        else: #초과
            j -= 1
    return len(people) - answer
