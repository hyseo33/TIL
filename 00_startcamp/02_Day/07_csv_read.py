# csv 파일 read의 2가지 방법

#1. split
# with open('lunch.csv', 'r', encoding='utf-8') as f:
#     lines = f.readlines() #list 형태
#     for line in lines:
#         #print(line.strip())
#         print(line.strip().split(',')) #.split : ,를 기준으로 나눠서 리스트로 형성해줌.


#2. csv reader

import csv

with open('lunch.csv', 'r', encoding='utf-8') as f:
    lines = csv.reader(f)

    for line in lines:
        print(line)
        