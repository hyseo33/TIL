#1-1. 파일 읽기(옛날 방식) - read()
# f = open('ssafy.txt', 'r')
# all_text = f.read() #f.read파일 내용 전체를 문자열로 리턴해줌
# print(all_text)
# f.close()

#1-2. 파일 읽기(최신 방식) - read()

# with open('with_ssafy.txt', 'r') as f:
#     all_text = f.read()
#     print(all_text)

#2-1. 파일 읽기(옛날 방식) - readlines() # 라인들을 읽어서 리스트로 만들어줌
# f = open('ssafy.txt', 'r')
# lines = f.readlines()

# for line in lines:
#     print(lines)
#     print(line)

# f.close()

#2-2. 파일 읽기(최신 방식) - readlines()

with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines() #print() 엔터의 의미
    for line in lines:
        print()
        print(line.strip()) #strip() 양쪽 공백 제거