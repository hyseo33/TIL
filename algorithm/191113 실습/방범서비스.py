import sys
sys.stdin = open('방범_input.txt')
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def security(x, y):
    global result

    Q = deque()
    Q.append([x, y])
    vis[x][y] = 1
    b_house = 0

    if data[x][y] == 1:
        b_house = 1

    while len(Q) != 0:
        spot = Q.popleft()
        x = spot[0]
        y = spot[1]
        if vis[x][y] == l:
            break

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if -1 < nx < N and -1 < ny < N:
                if vis[nx][ny] == 0:
                    vis[nx][ny] = vis[x][y]+1
                    if data[nx][ny] == 1:
                        b_house += 1
                    Q.append([nx, ny])

    if b_house * M >= l**2 + (l-1)**2:
        if b_house > result:
            result = b_house

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

    max_cost = house * M
    # print(max_cost)

    for k in range(1, 30):
        manage_cost = (k * k) + ((k-1) * (k-1))
        # print(manage_cost)
        # 지불할 수 있는 금액이 운영 비용보다 크면
        if max_cost < manage_cost:
            bound = k-1
            break
    result = 0
    # data의 각 지점 마다 bound 범위까지 bfs하기

    for l in range(bound, 0, -1):
        if result > 0:
            break
        for i in range(N):
            for j in range(N):
                vis = [[0] * N for _ in range(N)]
                security(i, j)


    print('#{} {}'.format(tc, result))

