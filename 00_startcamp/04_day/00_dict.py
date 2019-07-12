#1. 딕셔너리 만들기

lunch = {
    '중국집' : '02'
}

lunch = dict(중국집='02')
# print(lunch)

#2. 딕셔너리 내용 추가하기
lunch['분식집'] = '031'
# print(lunch)

idol = {
    'bts': {
        '지민': 24,
        'RM': 25
    }
}
#3. 딕셔너리 value 가져오기
# print(idol['bts']['RM']) # []로 접근해서 뽑아내기! bts를 고르니까 딕셔너리 나옴. 그래서 또 key를 써서 뽑아냄.
# print(idol.get('bts').get('RM')) #중간에 값이 없으면 []는 멈춤, .get은 넘어가서 error를 만들지 않음.

#4. 딕셔너리 반복문 활용하기
#4-1. 기본활용
# for key in lunch:
#     print(key)
#     print(lunch[key])

#4-2. .items() - key, value 모두 가져오기
# for key, value in lunch.items():
#     print(key, value)

#4-3. .values() - value만 가져오기
# for value in lunch.values():
#     print(value)

#4-4. .keys() - key만 가져오기
for key in lunch.keys():
    print(key)