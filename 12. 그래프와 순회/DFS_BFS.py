import sys
sys.stdin = open("input.txt", "r")

def dfs(c):
    ans_dfs.append(c)   # 방문 노드 추가
    v[c] = 1            # 방문 표시

    for n in adj[c]:
        if not v[n]:    # Next 노드를 아직 방문하지 않았다면
            dfs[n]

def bfs(s):
    q = list()

    q.append(s)         # queue에 초기데이터(들) 삽입, 단위작업
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]:  # 방문하지 않은 노드라면 노드 => 큐에 삽입한다.
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1



N, M, V = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(1, N + 1):
    adj[i].sort()

v = [0] * (N + 1)
ans_dfs = list()
dfs(v)

v = [0] * (N + 1)
ans_bfs = list()
bfs(v)

print(*ans_dfs)
print(*ans_bfs)

