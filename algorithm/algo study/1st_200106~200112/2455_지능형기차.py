import sys
sys.stdin = open('기차_input.txt')

person_info = []

for _ in range(4):
    person_info.append(list(map(int, input().split())))

temp = 0
max_people = 0

for i in range(4):
    temp -= person_info[i][0]
    temp += person_info[i][1]

    if temp > max_people:
        max_people = temp

print(max_people)