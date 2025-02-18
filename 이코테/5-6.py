# 인접행렬 (Adjacency Matrix)

INF = 999999999 # 인접행렬을 표현할 때 무한인 값은 다음과 같이 정의해준다.

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)