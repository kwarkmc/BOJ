from collections import deque


def solution(people, limit):
    queue = deque(sorted(people))

    result = 0

    while len(queue) > 1:
        # print(start, end)
        # 첫번째, 마지막 사람이 보트에 탈 수 있을 경우
        if queue[0] + queue[-1] <= limit:
            queue.pop()
            queue.popleft()
            result += 1
            # print("Two", start, end, result)
        else:
            queue.pop()
            result += 1
            # print("One", start, end, result)
    if queue:
        result += 1

    return result