import sys
sys.stdin = open('방범_input.txt')
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def security(x, y, N, b):
    Q = deque()
    Q.append([x, y])

    while len(Q) != 0:
        pass


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)

    house = 0 # 집 갯수
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                house += 1
    # print(house)

    total_cost = house * M
    print(total_cost)

    for k in range(1, 999):
        manage_cost = (k * k) + ((k-1) * (k-1))
        # print(manage_cost)
        # 지불할 수 있는 금액이 운영 비용보다 크면
        if total_cost < manage_cost:
            bound = k-1
            break

    # data의 각 지점 마다 bound 범위까지 bfs하기
    for i in range(N):
        for j in range(N):
            security(i, j, N, bound)

