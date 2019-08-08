from django.shortcuts import render
from decouple import config
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')

# 네이버 마마고 번역
def mamago(request):
    return render(request, 'utilities/mamago.html')

def translated(request):
    #1. 사용자가 입력한 한국어 텍스트
    word = request.GET.get('word')

    #2. 네이버에 번역 요청을 위해 필요한 준비
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')

    #3. 요청을 보낼 url
    mamago_url = 'https://openapi.naver.com/v1/papago/n2mt'

    #4. 헤어 정보 구성
    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret,
    }

    #5. 요청 데이터 준비
    data = {
        'source': 'ko',
        'target': 'en',
        'text': word,
    }

    #6. 네이버로 요청 보내기
    mamago_response = requests.post(mamago_url, headers=headers, data=data).json()
    # print(mamago_response)

    #7. 번역된 텍스트 값 뽑기
    eng_word = mamago_response.get('message').get('result').get('translatedText')

    context = {
        'kor_word': word,
        'eng_word': eng_word,
    }
    
    return render(request, 'utilities/translated.html', context)