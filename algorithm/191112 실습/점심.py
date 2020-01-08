import sys
sys.stdin = open('점심_input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def powerset(N, m):
    if N == m:
        print(A)
        lunch_time()
    else:
        A[m] = 1
        powerset(N, m + 1)
        A[m] = 0
        powerset(N, m + 1)

def lunch_time():
    dis = [] # 계단까지 가기
    step = [] # 계단 내려가기

    for i in range(len(A)):
        if A[i] == 0: # stair 0번째
            dx = abs(person[i][0] - stair[0][0])  # x
            dy = abs(person[i][1] - stair[0][1])  # y
            dis.append(dx + dy)
        else: # stair 1번째
            dx = abs(person[i][0] - stair[1][0])
            dy = abs(person[i][1] - stair[1][1])
            dis.append(dx + dy)
    print(dis)
    print()

    # t = 0
    # while True:
    #     for i in range(len(dis)):
    #         if dis[i] != 0:
    #             dis[i] -= 1
    #         elif dis[i] == 0 and len(step) < 3:
    #             dis[i] = 999
    #             if A[i] == 1:
    #                 step.append(stair[1][2])
    #             else:
    #                 step.append(stair[0][2])





T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 사람이랑 계단 찾기
    stair = []
    person = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                person.append([i, j])
            elif data[i][j] >= 2:
                stair.append([i, j, data[i][j]])

    # print(person)
    # print(stair)

    A = [0 for _ in range(len(person))]

    powerset(len(person), 0)

    print(t)
    # for i in range(len(person)):
    #     x = person[i][0]
    #     y = person[i][1]
    #     vis = [[0 for _ in range(N)] for _ in range(N)]


    # print('#{} {}'.format(tc, time))