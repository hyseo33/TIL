from itertools import combinations
import copy
import sys
sys.stdin = open('연구소_input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    Q = []
    Q.append([x, y])
    while len(Q) != 0:
        a = Q.pop(0)
        x = a[0]
        y = a[1]
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if -1 < nx < N and -1 < ny < M:
                if data[nx][ny] == 0:
                    data[nx][ny] = 2
                    Q.append([nx, ny])


N, M = map(int, input().split())

max_cnt = 0

# 1은 벽, 벽은 3개 꼭 추가, 2는 바이러스, 0이 최대가 되게 벽세우기
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))

blank = []
virus = []
for i in range(N):
    for j in range(M):
        if info[i][j] == 0:
            blank.append([i, j])
        elif info[i][j] == 2:
            virus.append([i, j])


blank_3 = list(combinations(blank, 3))


for i in range(len(blank_3)):
    data = copy.deepcopy(info)
    wall1 = blank_3[i][0]
    wall2 = blank_3[i][1]
    wall3 = blank_3[i][2]
    data[wall1[0]][wall1[1]] = 1
    data[wall2[0]][wall2[1]] = 1
    data[wall3[0]][wall3[1]] = 1

    for j in range(len(virus)):
        x = virus[j][0]
        y = virus[j][1]
        bfs(x, y)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)