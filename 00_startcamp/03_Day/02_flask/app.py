from flask import Flask, render_template, request
 # render_template를 불러와서 써야지만 html을 연결할 수 있다.

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', html_name=name) #html_name이 html 파일 안에 name은 여기에 있음

@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    return render_template('cube.html', result=result, number=number)

@app.route('/movie')
def movie():
    movies = ['토이스토리4', '스파이더맨', '비스트', '기생충', '알라딘', '마담싸이코', '라이온킹']
    return render_template('movie.html', movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('result') #repuest도 불러와야해. requests랑 달라.
    return render_template('pong.html', age=age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')