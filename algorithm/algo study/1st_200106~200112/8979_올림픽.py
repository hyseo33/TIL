import sys
sys.stdin = open('8979_input.txt')

## 8979_올림픽

N, K = map(int, input().split())
# N 국가의 수, K 등수를 알고 싶은 국가

nation_result = []

for _ in range(N):
    nation_result.append(list(map(int, input().split())))
    # 국가번호, 금, 은, 동

print(nation_result)

for i in range(N):
    nation = nation_result[i]
    m_num = 0
    score = 0
    for j in range(3):
        m_num += nation[j+1]
        score += (nation[j+1] * (3 - j))
    nation.append(m_num)
    nation.append(score)

sorted_result = sorted(nation_result, key=lambda x: x[1], reverse=True)

print(sorted_result)

rank = []

temp = 1

for i in range(N):
    sample = sorted_result[i]
    if 0 <= (i - 1) < N: