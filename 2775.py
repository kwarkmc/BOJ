T = int(input())

for _ in range(T):
    k = int(input())    # k층
    n = int(input())    # n호
    floor = list(range(1, n + 1))
    # new_floor = list([0] * n) 로 여기서 초기화 해줬었는데 오답이었음.
    # 아래 floor = new_floor 에서 새로운 객체인 new_floor에 값을 복사하는게 아니라 같은 객체로 설정해 버려서, 첫 Iter 만 정상적으로 작동하고, 그 다음부터 floor과 new_floor를 같은 객체로 처리해버리기 때문
    for i in range(k):
        new_floor = list([0] * n)   # 매 iter 마다 새로운 new_floor를 선언해서, L13에서 같은 객체로 할당하는 것을 막을 수 있다.
        for j in range(len(floor)):
            new_floor[j] = sum(floor[:j + 1])
        floor = new_floor

    print(floor[n - 1])