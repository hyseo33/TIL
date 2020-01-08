import sys
sys.stdin = open('숫자_input.txt')

def myprint(q):
    for i in range(q-1, -1, -1):
        print("%d " % t[i], end='')
    print()

def perm(n, r):
    if r == 0:
        # my_calc()
        myprint(N-1)
        # 하고싶은일
    else:
        for i in range(n-1, -1, -1):
            target_op[i], target_op[n-1] = target_op[n-1], target_op[i]
            t[r-1] = target_op[n-1]
            perm(n-1, r-1)
            target_op[i], target_op[n - 1] = target_op[n - 1], target_op[i]

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 숫자의 개수: 3이상 12이하
    operator = list(map(int, input().split())) # 연산자 개수의 총 합은 N-1
    # 순서대로 +(0), -(1), *(2), /(3)
    numbers = list(map(int, input().split())) # 숫자는 1 ~ 9

    # print(N)
    # print(operator)
    # print(numbers)
    # print(int(-2/3))
    min_value = 99999999999999999999
    max_value = 0

    t = [0] * (N -1)
    # 순열 만들 대상이 되는 연산자들, 총 개수: N-1
    target_op = []
    for i in range(4):
        n = operator[i]
        for _ in range(n):
            target_op.append(i)

    perm(N-1, N-1)

    # print(target_op)
    # print('#{} {}'.format(tc, max_value-min_value))
