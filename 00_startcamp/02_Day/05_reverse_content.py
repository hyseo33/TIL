#1. 각각의 라인을 리스트의 요소로 불러오기

with open('writelines_ssafy.txt', 'r') as f:
    lines = f.readlines() #f.redlines():f로 부른걸 리스트로 가져오기. 따라서 lines = 0 1 2 3

#2. 뒤집기    
    lines.reverse() #lines 자체를 바꾼다. 따라서 reverse는 리턴값이 없음. reversed는 원본을 그대로 두고 역순으로 뱉는다.

#3. line을 작성하기
with open('reversd_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)

    
 