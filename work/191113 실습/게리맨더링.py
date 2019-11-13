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

        check_connection(group0, group1)

    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

def check_connection(g0, g1):
    if len(g0) != 0:
        vis0 = [0] * len(g0)

    if len(g1) != 0:
       vis1 = [0] * len(g1)




T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 선거구수
    people = list(map(int, input().split())) # 각 선거구당 인구

    village_connect = [[0] * (N + 1) for _ in range(N + 1)]

    info = [] # 연결정보
    for i in range(N):
        info.append(list(map(int, input().split())))

    # print(village_connect)
    print(info)

    for j in range(len(info)):
        vil_cnt = info[j][0]
        for k in range(1, vil_cnt+1):
            village_connect[j+1][info[j][k]] = 1
            village_connect[info[j][k]][j+1] = 1

    A = [0] * N # 부분집합 준비

    powerset(N, 0)

    result = -1 # 기본값 -1, 두 선거구로 나눌 수 없으면 -1 그대로 출력