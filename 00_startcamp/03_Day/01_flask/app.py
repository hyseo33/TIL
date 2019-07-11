from flask import Flask
import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'
    
@app.route('/ssafy')
def ssafy():
    return 'This is ssafy!'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    endgame = datetime.datetime(2019, 11, 29)
    td = endgame - today
    return f'SSAFY 1학기 종료까지 {td.days} 일 남았습니다!'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag.</h1>'


@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄로 작성하자!</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """
# 동적인 routing : 내가 바꿀때마다 같이 바뀌어서 보여짐.

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다! {name}님!'

@app.route('/cube/<int:number>')
def mul(number):
    return f'{number}의 3제곱은 {number**3}입니다.'

# 점심 메뉴 list(5개)에서 2개(person)를 뽑아 출력하기

@app.route('/lunch/<int:person>') # int를 씌우면 자연수로 인식. 내가 입력한 값을 숫자로 바꿔줌
def food(person):
    lunch = ['라면','피자', '갈치', '소고기', '우동'] # ramdom은 항상 import로 가져오기. random.sample(어디서, 몇개)뽑기.
    menu = random.sample(lunch, person) #menu는 list의 형태, 마지막 print에서 str로 문자로 변경해주기.
    return f'오늘의 점심 메뉴는 {str(menu)}입니다.'