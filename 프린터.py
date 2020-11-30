#level2_stack/queue

def solution(priorities, location):
    answer = 0
    
    while priorities:
        if priorities[0] == max(priorities): #첫번째 원소가 가장 큰 우선순위 element일 때
            answer += 1
            priorities.pop(0) #queue처럼 항상 FIFO
            if location == 0:
                return answer
            else:
                location -= 1
                
        else:
            priorities.append(priorities.pop(0)) #맨뒤로 보내기
            if location == 0: #location은 0인데 가장 큰 우선순위가 아닐경우
                location = len(priorities)-1
            else:
                location -= 1
        
    return answer
