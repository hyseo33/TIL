import sys
sys.stdin = open('다리_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 세로, M 가로
    data = [list(map(int, input().split())) for _ in range(7)]

    print(data)
