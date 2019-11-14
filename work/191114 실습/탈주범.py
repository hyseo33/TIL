import sys
sys.stdin = open('탈주범_input.txt')
from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
# 상 좌 하 우

def search_man(x, y, i): # 가로 x, 세로 y, 터널 정보 i
    Q = deque()
    Q.append([x, y, i])
    vis[y][x] = 1

    while len(Q) != 0:
        t = Q.popleft()
        x = t[0]
        y = t[1]
        i = t[2]

        if vis[y][x] == L:
            break

        if i == 1: # 상하좌우
            for z1 in range(4):
                nx = x + dx[z1]
                ny = y + dy[z1]
                if -1 < nx < M and -1 < ny < N: # 범위 안에 들고
                    if vis[ny][nx] == 0 and info[ny][nx] != 0:
                        # 방문 안했고, 지하터널이 있을때
                        if check(nx, ny, z1):
                            # 지하터널이 연결이 되는지 확인
                            vis[ny][nx] = vis[y][x] + 1
                            Q.append([nx, ny, info[ny][nx]])

        elif i == 2: # 상하
            for z2 in range(0, 4, 2):
                nx = x + dx[z2]
                ny = y + dy[z2]
                if -1 < nx < M and -1 < ny < N:
                    if vis[ny][nx] == 0 and info[ny][nx] != 0:
                        if check(nx, ny, z2):
                            vis[ny][nx] = vis[y][x] + 1
                            Q.append([nx, ny, info[ny][nx]])

        elif i == 3: # 좌우
            for z3 in range(1, 4, 2):
                nx = x + dx[z3]
                ny = y + dy[z3]
                if -1 < nx < M and -1 < ny < N: # 범위 안에 들고
                    if vis[ny][nx] == 0 and info[ny][nx] != 0:
                        if check(nx, ny, z3):
                            vis[ny][nx] = vis[y][x] + 1
                            Q.append([nx, ny, info[ny][nx]])

        elif i == 4: # 상우
            for z4 in range(0, 4, 3):
                nx = x + dx[z4]
                ny = y + dy[z4]
                if -1 < nx < M and -1 < ny < N: # 범위 안에 들고
                    if vis[ny][nx] == 0 and info[ny][nx] != 0:
                        if check(nx, ny, z4):
                            vis[ny][nx] = vis[y][x] + 1
                            Q.append([nx, ny, info[ny][nx]])

        elif i == 5: # 하우
            for z5 in range(2, 4):
                nx = x + dx[z5]
                ny = y + dy[z5]
                if -1 < nx < M and -1 < ny < N: # 범위 안에 들고
                    if vis[ny][nx] == 0 and info[ny][nx] != 0:
                        if check(nx, ny, z5):
                            vis[ny][nx] = vis[y][x] + 1
                            Q.append([nx, ny, info[ny][nx]])

        elif i == 6: # 하좌
            for z6 in range(1, 3):
                nx = x + dx[z6]
                ny = y + dy[z6]
                if -1 < nx < M and -1 < ny < N: # 범위 안에 들고
                    if vis[ny][nx] == 0 and info[ny][nx] != 0:
                        if check(nx, ny, z6):
                            vis[ny][nx] = vis[y][x] + 1
                            Q.append([nx, ny, info[ny][nx]])

        elif i == 7: # 상좌
            for z7 in range(0, 2):
                nx = x + dx[z7]
                ny = y + dy[z7]
                if -1 < nx < M and -1 < ny < N:  # 범위 안에 들고
                    if vis[ny][nx] == 0 and info[ny][nx] != 0:
                        if check(nx, ny, z7):
                            vis[ny][nx] = vis[y][x] + 1
                            Q.append([nx, ny, info[ny][nx]])

up = [1, 2, 5, 6] # 위로 갈땐 얘네들 있어야 가능
down = [1, 2, 4, 7]
left = [1, 3, 4, 5]
right = [1, 3, 6, 7]


def check(x, y, d):
    if d == 0: # 상
        if info[y][x] in up:
            return True
    elif d == 1: # 좌
        if info[y][x] in left:
            return True
    elif d == 2: # 하
        if info[y][x] in down:
            return True
    elif d == 3: # 우
        if info[y][x] in right:
            return True
    return False

T = int(input())

for tc in range(1, T+1):
    # 지하터널 세로 N, 가로 M, 맨홀 위치 세로 R, 가로 C, 소요 시간 L
    N, M, R, C, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]

    vis = [[0] * M for _ in range(N)]

    # print(N, M, R, C, L)
    # print(info)
    # print(vis)

    hole = [R, C] # 맨홀 위치(시작)

    search_man(C, R, info[R][C])

    cnt = 0

    for i in range(M):
        for j in range(N):
            if vis[j][i] != 0:
                cnt += 1
    # [print(vis[i]) for i in range(len(vis))]
    print('#{} {}'.format(tc, cnt))
