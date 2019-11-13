import sys
sys.stdin = open('숫자_input.txt')

def my_calc(num, idx, k):

    global max_value, min_value

    if k == N-1:

        if max_value < num:
            max_value = num
        if min_value > num:
            min_value = num


    for i in range(4):
        if operator[i] != 0:
            if i == 0: # +
                operator[i] -= 1
                my_calc(num + numbers[idx + 1], idx + 1, k+1)
                operator[i] += 1
            elif i == 1: # -
                operator[i] -= 1
                my_calc(num - numbers[idx + 1], idx + 1, k+1)
                operator[i] += 1
            elif i == 2: # *
                operator[i] -= 1
                my_calc(num * numbers[idx + 1], idx + 1, k+1)
                operator[i] += 1
            elif i == 3: # /
                operator[i] -= 1
                my_calc(int(num / numbers[idx + 1]), idx + 1, k+1)
                operator[i] += 1

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 숫자의 개수: 3이상 12이하
    operator = list(map(int, input().split())) # 연산자 개수의 총 합은 N-1
    # 순서대로 +(0), -(1), *(2), /(3)
    numbers = list(map(int, input().split())) # 숫자는 1 ~ 9
    max_value = -999999999
    min_value = 999999999


    # print(N)
    # print(operator)
    # print(numbers)

    my_calc(numbers[0], 0, 0)

    # print(max_value)
    # print(min_value)
    print('#{} {}'.format(tc, max_value - min_value))
