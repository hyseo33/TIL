import sys
sys.stdin = open('다리_input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, s):
    vis[x][y] = s

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if -1 < nx < N and -1 < ny < M:
            if data[nx][ny] == 1 and vis[nx][ny] == 0:
                dfs(nx, ny, s)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 세로, M 가로
    data = [list(map(int, input().split())) for _ in range(7)]



    s = 0 # 섬 개수 세기
    print(data)

    vis = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if data[i][j] == 1 and vis[i][j] == 0:
                s += 1
                dfs(i, j, s)

    connect_info = [[9874568] * (s+1) for _ in range(s+1)]

    [print(vis[i]) for i in range(len(vis))]
    print(s)

