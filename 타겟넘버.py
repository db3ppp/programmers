#DFS/BFS_level2

def solution(numbers, target):
    answer = 0
    tree = [0]
    
    for num in numbers:
        temp = []
        for element in tree:
            temp.append(element + num)
            temp.append(element - num)
        tree = temp
        
    answer = tree.count(target)
    return answer
