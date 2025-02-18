# BFS (Breadth First Search)

'''
1. 탐색 시작 노드를 큐에 넣고 방문 처리
2. 큐에서 노드 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드 모두 큐에 삽입, 방문 처리
3. 2번 과정 더 이상 수행할 수 없을 때 까지 반복
'''

from collections import deque

def bfs(graph, start, visited):
    # 1. 탐색 시작 노드를 큐에 넣고 방문 처리
    queue = deque([start])
    visited[start] = True
    while queue:
        # 2. 큐에서 노드 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드 모두 큐에 삽입, 방문 처리
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)