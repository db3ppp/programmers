#stack/queue_level2

import math 
def solution(progresses, speeds):
    answer = []
    diff = [math.ceil((100-x)/y) for x, y in zip(progresses, speeds)]
    
    while len(diff) > 0:
        a = diff.pop(0)
        Q = diff.copy()
        
        cnt = 1
        for i in range(len(diff)):
            if a >= diff[i]:
                cnt += 1
                Q.pop(0) #계산된거는 큐에서 제거
            else:
                break
        
        answer.append(cnt)
        diff = Q.copy()
    return answer
