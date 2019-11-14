import sys
sys.stdin = open('요리사_input.txt')
from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    # print(info)

    min_gap = 9879987987

    # 총 식재료 수 N
    # 선택할 식재료 수 N // 2
    total_elem = [i for i in range(N)]
    # print(total_elem)

    # 선택된 식재료 조합 -> A
    selec_elem = list(combinations(total_elem, N//2))
    # print(selec_elem)
    # print(len(selec_elem)//2)


    for i in range(len(selec_elem)//2):
        A = selec_elem[i]
        B = selec_elem[len(selec_elem) -1 -i]
        cook_A = 0
        cook_B = 0
        for a in range(len(A) - 1):
            for aa in range(a + 1, len(A)):
                cook_A += info[A[a]][A[aa]]
                cook_A += info[A[aa]][A[a]]
                cook_B += info[B[a]][B[aa]]
                cook_B += info[B[aa]][B[a]]
        gap = abs(cook_A - cook_B)
        if gap < min_gap:
            min_gap = gap

    print('#{} {}'.format(tc, min_gap))

