from flask import Flask, render_template, request #request는 요청한 것 받기
from bs4 import BeautifulSoup
import requests #requests는 요청하기(crawling 할 때 사용했던..)

app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    num = request.args.get('num')
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    lotto = res.json() #딕셔너리 형태로 바꿔줌 .json()을 쓰면 json형태의 자료를 딕셔너리로 변경해줌.

    #1. 번호 6개 가져오기
    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])

    #2. 내 번호 리스트 만들기
    numbers = []
    for num in request.args.get('numbers').split():
        numbers.append(int(num))

    if len(numbers) == 6:
        #번호 교집합 개수 찾기.
        matched = 0
        for num in numbers:
            if num in winner:
                matched += 1
        if matched == 6:
            result = '1등입니다!!!!!(퇴사가능)'
        elif matched == 5:
            if lotto['bnusNo'] in numbers:
                result = '2등입니다!!!!(새차가즈아)'
            else:
                result = '3등입니다!!!(소고기가능)'
        elif matched == 4:
            result = '4등입니다.(택시타염)'
        elif matched == 3:
            result = '5등입니다.(재도전)'
        else:
            result = '꽝입니다.(돈날림)'      

    else:
        result = '6개를 입력하시오.'
    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)