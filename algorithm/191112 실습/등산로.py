import sys
sys.stdin = open('등산로_input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0] #상하좌우 찾기

def find_road(x, y, t_road):
    global max_road

    if t_road > max_road:
        max_road = t_road

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if -1 < nx < N and -1 < ny < N:
            if data[nx][ny] < data[x][y]:

                find_road(nx, ny, t_road + 1)


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) # N: 한변의 길이, K: 최대 공사 가능 깊이
    data = [list(map(int, input().split())) for _ in range(N)]

    max_h = 0
    max_road = 0

    for i in range(N):
        for j in range(N):
            if data[i][j] >= max_h:
                max_h = data[i][j]

    start_point = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == max_h:
                start_point.append([i, j])

    for i in range(N):
        for j in range(N):
            for k in range(1, K+1):
                data[i][j] -= k

                for l in range(len(start_point)):

                    x = start_point[l][0]
                    y = start_point[l][1]

                    find_road(x, y, 1)

                data[i][j] += k

    print('#{} {}'.format(tc, max_road))