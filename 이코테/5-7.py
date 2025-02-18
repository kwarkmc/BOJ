# 인접 리스트 (Adjacency List)
# -> 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장한다.
# 원래는 연결리스트 자료형을 사용하여 구현해야 하지만, 파이썬에서는 배열의 크기가 상관 없는 append 매서드를 사용할 수 있기 때문에 그냥 리스트 자료형을 사용한다.

graph = [[] for _ in range(3)]  # 행이 3개인 2차원 리스트로 인접 리스트 표현

graph[0].append((1, 7)) # 노드 / 거리
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)

