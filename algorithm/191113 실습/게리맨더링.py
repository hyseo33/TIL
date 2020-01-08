import sys
sys.stdin = open('게리맨더링_input.txt')

def powerset(n, k):
    if n == k:
        group0 = []
        group1 = []
        for i in range(N):
            if A[i] == 0:
                group0.append(i+1)
            else:
                group1.append(i+1)

        if len(group0) == N or len(group1) == N:
            return
        check_connection(group0, group1)

    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

def dfs(x, s, vis, g): # 시작, 구별, 방문list, 소속그룹
    vis[x] = s
    for i in range(1, len(village_connect[x])):
        if i in g:
            if village_connect[x][i] == 1 and vis[i] == 9:
                dfs(i, s, vis, g)


def check_connection(g0, g1):
    vis = [9] * (N+1)
    # print(g0)
    # print(g1)
    p0 = g0[0]
    p1 = g1[0]

    dfs(p0, 0, vis, g0)
    dfs(p1, 1, vis, g1)

    cnt0 = 0
    cnt1 = 0
    for i in range(len(vis)):
        if vis[i] == 0:
            cnt0 += 1
        if vis[i] == 1:
            cnt1 += 1

    if cnt0 == len(g0) and cnt1 == len(g1):
        # 사람 수 세기
        calc_people(g0, g1)

def calc_people(g0, g1):
    global min_gap

    people0 = 0
    people1 = 0

    for i in range(len(g0)):
        people0 += people[g0[i] - 1]

    for j in range(len(g1)):
        people1 += people[g1[j] - 1]

    p_gap = abs(people0 - people1)
    if p_gap < min_gap:
        min_gap = p_gap

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 선거구수
    people = list(map(int, input().split())) # 각 선거구당 인구

    village_connect = [[0] * (N + 1) for _ in range(N + 1)] # 인접행렬

    info = [] # 연결정보
    for i in range(N):
        info.append(list(map(int, input().split())))

    # print(village_connect)
    # print(info)

    # 연결정보로부터 인접행렬 만들기
    for j in range(len(info)):
        vil_cnt = info[j][0]
        for k in range(1, vil_cnt+1):
            village_connect[j+1][info[j][k]] = 1
            village_connect[info[j][k]][j+1] = 1

    A = [0] * N # 부분집합 준비

    min_gap = 987988798

    powerset(N, 0)

    if min_gap == 987988798:
        min_gap = -1

    print(min_gap)