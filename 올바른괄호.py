#연습문제_level2

def solution(s):
    answer = True
    stack = []
    
    for character in s:
        if character == "(": #괄호시작만 stack에 넣기
            stack.append(character)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        
    return len(stack) == 0 #stack이 empty여야 true
