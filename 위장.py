#해시_level2

def solution(clothes):
    answer = 1
    closet = {} #for dictionary
    
    for element in clothes:
        value = element[0]
        key = element[1]
        
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]

    for key in closet:
        answer *= (len(closet[key]) +1)
    return answer -1 #하나도 안입는 경우 제외
