# 파이썬 코드로 텔레그램 메세지 보내기
from decouple import config
import requests

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN') #보안이 너무 취약해 토큰과 아이디가 다 알려짐. 따라서 python decouple을 깔자.
chat_id = config('CHAT_ID')
text = '오늘 삼계탕 먹나유?'

send_message = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message.text)
