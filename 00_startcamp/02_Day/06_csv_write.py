# csv는 딕셔너리로 조작

lunch = {
    '양자강' : '02-542-4322',
    '김밥카페' : '02-334-2394',
    '순남시레기' : '03-452-1235'
}
#1. 방법 1 

with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
       # print(type(item))
        f. write(f'{item[0]}, {item[1]}\n') # .items : 튜플라는 자료형으로 뱉음. ()소괄호 형태로 값이 들어가게됨 ex. ('1', '2', '3')
        