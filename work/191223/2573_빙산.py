import sys
sys.stdin = open('빙산_input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def counting(i, j): # 빙산 옆 바다를 세서 저장
    Q = deque()
    Q.append([i, j])
    vis[i][j] = -1

    sea_info = [[0] * M for _ in range(N)]

    while Q:
        q = Q.popleft()
        sea = 0
        vis[q[0]][q[1]] = -1
        for z in range(4):
            nx = q[0] + dx[z]
            ny = q[1] + dy[z]
            if -1 < nx < N and -1 < ny < M:
                if ice[nx][ny] == 0:
                    sea += 1
                elif ice[nx][ny] > 0 and vis[nx][ny] == 0:
                    Q.append([nx, ny])

        sea_info[q[0]][q[1]] = sea

    melt(sea_info)

def melt(arr): # 녹이고
    ice_nums = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if ice[i][j] > 0:
                ice[i][j] -= arr[i][j]
                if ice[i][j] < 0:
                    ice[i][j] = 0
                elif ice[i][j] > 0:
                    ice_nums += 1

    check(ice, ice_nums)

def check(arr, nums): # 하나인지 확인
    global flag

    vis1 = [[0] * M for _ in range(N)]

    Q = deque()
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] > 0 and vis1[i][j] == 0:
                cnt1 = 0
                Q.append([i, j])
                vis1[i][j] = 9
                cnt1 += 1
                while Q:
                    q = Q.popleft()
                    for z in range(4):
                        nx = q[0] + dx[z]
                        ny = q[1] + dy[z]
                        if -1 < nx < N and -1 < ny < M:
                            if arr[nx][ny] > 0 and vis1[nx][ny] == 0:
                                Q.append([nx, ny])
                                vis1[nx][ny] = 9
                                cnt1 += 1
                if cnt1 < nums:
                    flag = 1
                    return



N, M = map(int, input().split()) # 행, 열

ice = []
for i in range(N):
    ice.append(list(map(int, input().split())))

result = 0

flag = 0

while not flag:
    result += 1
    vis = [[0] * M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if ice[i][j] > 0 and vis[i][j] == 0:
                counting(i, j)


print(result)