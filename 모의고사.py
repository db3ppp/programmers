#완전탐색_level1

def solution(answers):
    answer = []
    answer_temp = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    score1 = score2 = score3 = 0
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            score1+=1
        if answers[i] == two[i % len(two)]:
            score2+=1
        if answers[i] == three[i % len(three)]:
            score3+=1
    
    max_score = max(score1, score2, score3)
    if max_score == score1:
        answer.append(1)
    if max_score == score2:
        answer.append(2)
    if max_score == score3:
        answer.append(3)
        
#    answer_temp = [score1, score2, score3]
#    for person, score in enumerate(answer_temp):
#        if score == max_score:
#            answer.append(person+1)
        
    return answer
