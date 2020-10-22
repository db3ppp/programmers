#DFS/BFS_level3

def solution(n, computers):
    answer = 0
    bfs = [] #empty queue
    visited = [0]*n
    
    while 0 in visited: #모두 방문할 때 까지
        x = visited.index(False)
        bfs.append(x)
        visited[x] = True
        
        while bfs:
            node = bfs.pop(0) #큐에서 꺼내기
            visited[node] = True
            for i in range(n):
                if visited[i] == False and computers[node][i] == 1:#아직 안방문했고, 이어져있는 노드면
                    bfs.append(i) #큐에 추가
                    visited[i] = True
                
        answer += 1
    return answer
