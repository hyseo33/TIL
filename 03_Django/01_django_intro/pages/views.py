from django.shortcuts import render
from datetime import datetime
import random
import requests

# Create your views here.

#1. 기본 로직
def index(request):
    return render(request, 'pages/index.html')

def introduce(request):
    return render(request, 'pages/introduce.html')

def images(request):
    return render(request, 'pages/images.html')

#2. 템플릿 변수(Template Variable)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '피자', '엉터리 쌩고기', '떡볶이']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)

#3. 동적 라우팅(Varialbe Routing)
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '피자', '엉터리 쌩고기', '떡볶이']
    pick = random.choice(menu)
    context = {'name': name, 'age': age, 'pick': pick}
    return render(request, 'pages/hello.html', context)

#4. 실습
#4-1. 동적 라우팅을 활용해서(name과 age를 인자로 받아) 자기소개 페이지
def introduce2(request, name, age):
    context = {'name': name, 'age': age}
    return render(request, 'pages/introduce2.html', context)

#4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def multi(request, num1, num2):
    num3 = num1 * num2
    context = {'result': num3, 'num1': num1, 'num2': num2}
    return render(request, 'pages/multi.html', context)

#4-3. 반지름을 인자로 받아 원의 넓이를 구하시오.
def circle(request, r):
    area = 3.14 * r * r
    context = {'area': area, 'r': r}
    return render(request, 'pages/circle.html', context)

#5. DTL(Django Temolate Language)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '유린기']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'watermelon', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'pages/template_language.html', context)

#6. 실습
#6-1. isbirth

def isbirth(request):
    today = datetime.now()

    if today.month == 9 and today.day == 18:
        result = True
    else:
        result = False

    context = {
        'result': result,
    }
    return render(request, 'pages/isbirth.html', context)


#6-2. 회문판별(palindrome)
#회문이면 회문입니다. 회문이 아니면 회문이 아닙니다.

def ispal(request, words):
    rev_words = words[::-1]

    if words == rev_words:
        result = True
    else:
        result = False

    context = {'result': result}
    return render(request, 'pages/ispal.html', context)

'''
# 스앵님 풀이
def ispal(request, words):
    result = False
    if words == words[::-1]:
        result = True
    context = {
        'words': words,
        'result': result,
    }
    return render(request, 'ispal.html', context)
'''

#6-3. 로또 번호 추첨
# lottos -> 1~45까지의 번호 중 6개를 랜덤으로 pick한 리스트
# real_lottos -> [21, 24, 30, 32, 40, 42]
#1. lottos 번호를 DTL(for문) 문법을 활용해 하나씩 출력 해보기
#2. 컴퓨터가 뽑은 로또 번호와 실제 로또 당첨 번호를 비교해보기(DTL-if문)

def lotto(request):
    real_lottos = [21, 24, 30, 32, 40, 42]
    lottos = list(random.sample(range(1,46), 6))

    context = {
        'real_lottos': real_lottos,
        'lottos': lottos,
    }

    return render(request, 'pages/lotto.html', context)
    
    # if real_lottos == lottos:
    #     result = True
    # else:
    #     result = False


#7. Form - GET(데이터를 조회할 때, html파일 하나 줘.) get방식은 입력값이 주소창에 노출된다.
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'pages/catch.html', context)

# 연습하기
def ping(request):
    return render(request,'pages/ping.html')

def pong(request):
    text = request.GET.get('ping') #'ping'박스를 열어서 text라는 변수에 담았고..
    context = {
        'abc': text 
    }
    return render(request, 'pages/pong.html', context)

#8. Form - GET 실습(아스키 아티)
def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form으로 날린 데이터를 받는다.(GET)
    word = request.GET.get('word')
    #2. ARTII api로 요청을 보내 응답 결과를 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    #3. fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')
    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서 font라는 변수(str)에 저장한다.
    font = random.choice(fonts)
    #5. 사용자에게 입력받은 word와 font를 가지고 다시 요청을 보낸다.
    #그리고 응답 결과를 result에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {
        'result': result,
    }
    return render(request, 'pages/result.html', context)

#9. Form - POST
def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'password': pwd,
    }
    return render(request, 'pages/user_create.html', context)

# 190807
#10. 정적 파일
def static_ex(request):
    return render(request, 'pages/static_ex.html')