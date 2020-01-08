import sys
sys.stdin = open('자석_input.txt')
from collections import deque

def check(t):

    neighbor.append(t)

    if t == 1: # 첫번째
        while t < 4:
            if magnetic[t][2] != magnetic[t+1][6]:
                neighbor.append(t+1)
                t += 1
            else:
                break

    elif t == 4: # 마지막
        while t > 0 :
            if magnetic[t][6] != magnetic[t-1][2]:
                neighbor.append(t-1)
                t -= 1
            else:
                break

    else: # 2, 3
        fix_t = t # 2, 3 둘중에 표시

        while t < 4: # 오른쪽 확인
            if magnetic[t][2] != magnetic[t+1][6]:
                neighbor.append(t+1)
                t += 1
            else:
                break

        t = fix_t
        while 0 < t <= 4: # 왼쪽 확인

            if magnetic[t][6] != magnetic[t-1][2]:
                neighbor.append(t-1)
                t -= 1
            else:
                break

a = [0, 1, -1, 1, -1]
b = [0, -1, 1, -1, 1]

def cycle_d(targets, d): #3, -1
    # 방향 짝지어주기
    if a[targets[0]] == d:
        for i in range(len(targets)):
            m_d_pair.append([targets[i], a[targets[i]]])

    else:
        for j in range(len(targets)):
            m_d_pair.append([targets[j], b[targets[j]]])

T = int(input())

for tc in range(1, T+1):
    K = int(input()) # K 회전 횟수
    # 0은 N, 1은 S
    magnetic = [deque([9, 9, 9, 9, 9, 9, 9, 9])] + [deque(map(int, input().split())) for _ in range(4)]
    # 자석번호, 방향(1 시계, -1 반시계)
    cycle_info = [list(map(int, input().split())) for _ in range(K)]

    # print(magnetic)
    # print(cycle_info)
    # for i in range(1, len(magnetic)):
    #     print(magnetic[i])

    for i in range(K):
        target = cycle_info[i][0] # 회전 대상 자석
        direction = cycle_info[i][1] # 방향 1, -1

        neighbor = [] # 회전 대상 자석

        # 빡친다 빢쳐 하드코딩밖에 생각이 안나!!!!!! 박대가리 같으니라고
        check(target)

        m_d_pair = [] # 마그넷이랑 방향 페어

        cycle_d(neighbor, direction)

        # print(m_d_pair)

        for j in range(len(m_d_pair)):
            num = m_d_pair[j][0]
            direc = m_d_pair[j][1]

            if direc == 1: # 시계
                p = magnetic[num].pop()
                magnetic[num].appendleft(p)
            else: # 반시계
                pp = magnetic[num].popleft()
                magnetic[num].append(pp)

        # [print(magnetic[i]) for i in range(len(magnetic))]
        # print()

    score = 0
    # 점수 계산하기
    for i in range(1, len(magnetic)):
        if magnetic[i][0] == 1:
            if i == 1:
                score += 1-
            elif i == 2:
                score += 2
            elif i == 3:
                score += 4
            elif i == 4:
                score += 8

    print('#{} {}'.format(tc, score))