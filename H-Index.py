#정렬_level2

def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(len(citations)+1):
        count = 0
        for value in citations:
            if value >= i:
                count += 1
                
        if count >= i: # h>=n
            answer = i
    return answer
