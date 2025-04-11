import sys
from collections import deque

# sys.stdin = open("input.txt", 'r')

def bfs(root):

    if root == delete_node:
        return 0

    queue = deque()
    queue.append(root)
    leaf_count = 0

    while queue:
        curr = queue.popleft()

        if not tree[curr] or (len(tree[curr]) == 1 and tree[curr][0] == delete_node):
            leaf_count += 1
            continue

        for child in tree[curr]:
            if child != delete_node:
                queue.append(child)

    return leaf_count


N = int(sys.stdin.readline())
tree = [[] for _ in range(N)]
root = -1

array_input = list(map(int, sys.stdin.readline().rstrip().split()))

for child, parent in enumerate(array_input):
    if parent == -1:
        root = child
    else:
        tree[parent].append(child)


delete_node = int(sys.stdin.readline()) # 지울 번호

print(bfs(root))


