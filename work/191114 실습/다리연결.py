import sys
sys.stdin = open('다리_input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 상 하 좌 우

def dfs(y, x, s):
   vis[y][x] = s

   for z in range(4):
       nx = x + dx[z]
       ny = y + dy[z]
       if -1 < nx < M and -1 < ny < N:
           if data[ny][nx] == 1 and vis[ny][nx] == 0:
               dfs(ny, nx, s)

def cnt_length(y, x, d):
    global cnt, reach

    if d == 0: # 상
        while y != -1:
            if y == 0:
                if vis[y][x] == 0:  # 섬 못만남
                    cnt = 0
                    return
                elif vis[y][x] != 0:
                    reach = vis[y][x]
                    return
            elif y > 0:
                if vis[y][x] == 0:  # 아직 바다임
                    cnt += 1
                    y -= 1
                elif vis[y][x] != 0:  # 섬 만남
                    reach = vis[y][x]
                    return

    elif d == 1: # 하
        while y != N:
            if y == N-1:
                if vis[y][x] == 0:  # 섬 못만남
                    cnt = 0
                    return
                elif vis[y][x] != 0:
                    reach = vis[y][x]
                    return
            elif y < N:
                if vis[y][x] == 0:  # 아직 바다임
                    cnt += 1
                    y += 1
                elif vis[y][x] != 0:  # 섬 만남
                    reach = vis[y][x]
                    return

    elif d == 2: # 좌
       while x != -1:
           if x == 0:
               if vis[y][x] == 0: # 섬 못만남
                   cnt = 0
                   return
               elif vis[y][x] != 0:
                   reach = vis[y][x]
                   return
           elif x > 0:
               if vis[y][x] == 0: # 아직 바다임
                   cnt += 1
                   x -= 1
               elif vis[y][x] != 0: # 섬 만남
                   reach = vis[y][x]
                   return

    elif d == 3: # 우
        while x != M:
            if x == M-1:
                if vis[y][x] == 0:  # 섬 못만남
                    cnt = 0
                    return
                elif vis[y][x] != 0:
                    reach = vis[y][x]
                    return
            elif x < M:
                if vis[y][x] == 0:  # 아직 바다임
                    cnt += 1
                    x += 1
                elif vis[y][x] != 0:  # 섬 만남
                    reach = vis[y][x]
                    return

T = int(input())
for tc in range(1, T+1):
   N, M = map(int, input().split()) # N 세로, M 가로
   data = [list(map(int, input().split())) for _ in range(7)]
   s = 0 # 섬 개수 세기
   # print(data)
   vis = [[0] * M for _ in range(N)]
   for i in range(N): # 세로
       for j in range(M): # 가로
           if data[i][j] == 1 and vis[i][j] == 0:
               s += 1
               dfs(i, j, s)

   # 섬 사이 다리 연결 정보
   connect_info = [[99] * (s+1) for _ in range(s+1)]

   [print(vis[i]) for i in range(len(vis))]
   # print(s)
   # print(connect_info)
   for t in range(1, s+1):
       for i in range(N): # 세로
           for j in range(M): # 가로
               if vis[i][j] == t:
                   for z in range(4):
                       ni = i + dy[z]
                       nj = j + dx[z]
                       if -1 < ni < N and -1 < nj < M: # 인덱스 범위
                           if vis[ni][nj] == 0: # 바다가 맞으면
                               cnt = 0
                               reach = 0 # 닿은 섬 정보

                               cnt_length(ni, nj, z)

                               if cnt != 0:
                                   if cnt == 1:
                                       connect_info[t][reach] = 99
                                   elif connect_info[t][reach] > cnt:
                                       connect_info[t][reach] = cnt
                               elif cnt == 0:
                                   continue

   [print(connect_info[i]) for i in range(len(connect_info))]
   print()

   min_bridge = 0

   # if sum(connect_info) == (99 * (s+1) * (s+1)):
   #     min_bridge = -1
   # else:
   #     pass
   #
   # print('#{} {}'.format(tc, min_bridge))