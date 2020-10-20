#정렬_level1

def solution(array, commands):
    answer = []
    lst = []
    for comm in commands:
        start = comm[0]
        end = comm[1]
        val = comm[2]
    #for i in range(len(commands)):
        #start = commands[i][0]
        #end = commands[i][1]
        #val = commands[i][2]
        
        lst = array[start-1:end]
        lst.sort()
        value = lst[val-1]
        answer.append(value)
    return answer
