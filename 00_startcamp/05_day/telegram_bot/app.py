from flask import Flask, render_template, request
from decouple import config #.env 파일에 기록한 토큰과 챗아이디를 가져오자.
import requests

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')

    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
4
    return render_template('send.html')

    # ngrok으로 네트워크 연결하기.

@app.route(f'/{token}', methods=['POST'])
def telegram():
    #1. 구조 print 해보기 & 변수 저장
    # print(request.get_json())
    # print(type(request.get_json())) #json 형태의 자료를 dict로 바꿔줌. 우리가 python에서 조작할 수 있도록
    from_telegram = request.get_json()

    #2. 메세지를 그대로 돌려보내기
    if from_telegram.get('message') is not None:
        chat_id = from_telegram.get('message').get('from').get('id') #.get()은 빈칸이라도 에러안남!
        # print(chat_id)
        text = from_telegram.get('message').get('text')
        

        #3. Keyword(번역)
        if text[0:4] == '/번역 ':
            headers = {'X-Naver-Client-Id': naver_client_id, 'X-Naver-Client-Secret': naver_client_secret}
            data = {'source': 'ko', 'target': 'en', 'text': text[4:]} # 필수 요청 사항 3개. source, target, text

            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            print(papago_res)
            text = papago_res.json().get('message').get('result').get('translatedText') #이 줄의 text는 번역된 결과
            print(text)
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')


    return '', 200
    