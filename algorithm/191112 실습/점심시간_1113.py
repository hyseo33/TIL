import sys

sys.stdin = open('점심_input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def powerset(N, m):
    if N == m:
        lunch_time()
    else:
        A[m] = 1
        powerset(N, m + 1)
        A[m] = 0
        powerset(N, m + 1)


def lunch_time():
    global final_t

    dis = []  # 모든 애들 계단까지 가기
    for i in range(len(A)):
        if A[i] == 0:  # stair 0번째 가는 애들
            dx = abs(person[i][0] - stair[0][0])  # x
            dy = abs(person[i][1] - stair[0][1])  # y
            dis.append(dx + dy)
        else:  # stair 1번째
            dx = abs(person[i][0] - stair[1][0])
            dy = abs(person[i][1] - stair[1][1])
            dis.append(dx + dy)
    # print(dis)
    # print()

    step0 = []  # 0번 계단 내려가기
    step1 = []  # 1번 계단 내려가기

    for j in range(len(dis)):
        if A[j] == 1:  # 1번 가는 애들
            step1.append(dis[j])
        elif A[j] == 0:  # 0번 가는 애들
            step0.append(dis[j])

    step0 = sorted(step0)  # 차례대로 서고
    step1 = sorted(step1)

    # print(step0)
    # print(step1)

    # 이제 시간 재자

    t0 = [0] * 500
    t1 = [0] * 500


    for a in range(len(step0)):  # 0번 계단 시간
        s0 = step0[a]
        if t0[s0] < 3:
            for aa in range(stair[0][2]):
                t0[s0 + aa] += 1
        elif t0[s0] >= 3:
            while t0[s0] >= 3:
                s0 += 1
            for aa in range(stair[0][2]):
                t0[s0 + aa] += 1

            # for aaa in range(s0+1, len(t0)):
            #     if t0[aaa] < 3:
            #         for aa1 in range(stair[0][2]):
            #             t0[aaa+aa1] += 1
    tt0 = 0
    for a1 in range(len(t0)):
        if t0[a1] != 0:
            tt0 = a1

    for b in range(len(step1)):  # 1번 계단
        s1 = step1[b]
        if t1[s1] < 3:
            for bb in range(stair[1][2]):
                t1[s1 + bb] += 1
        elif t1[s1] >= 3:
            while t1[s1] >= 3:
                s1 += 1
            if t1[s1] < 3:
                for bb in range(stair[1][2]):
                    t1[s1 + bb] += 1

    tt1 = 0
    for b1 in range(len(t1)):
        if t1[b1] != 0:
            tt1 = b1

    # 0번, 1번 계단 시간중에 더 느린애 final에 담기
    if tt0 > tt1:
        if final_t > tt0:
            final_t = tt0
    else:
        if final_t > tt1:
            final_t = tt1

    # if(final_t==6):
    #     print(step0)
    #     print(t0)
    #     print(stair[0][2])
    #     print(step1)
    #     print(t1)
    #     print(stair[1][2])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 바보들 다 내려가는 시간
    final_t = 999999999999999999999

    # 사람이랑 계단 찾기
    stair = []
    person = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                person.append([i, j])
            elif data[i][j] >= 2:
                stair.append([i, j, data[i][j]])
    # print(stair)

    # 부분집합 만들 준비
    A = [0 for _ in range(len(person))]

    powerset(len(person), 0)

    print('#{} {}'.format(tc, final_t + 2))
