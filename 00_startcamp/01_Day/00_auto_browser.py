import webbrowser

# webbrowser.open('https://google.com')
# webbrowser.open_new('https://www.naver.com')
# webbrowser.open_new_tab('http://www.daum.net')

lists=['bts', '야호', '아침밥', '졸려']
for list in lists: #lists에 있는 애들을 다 쓸때까지 반복
    # print(type(list)
    webbrowser.open('https://search.naver.com/search.naver?&query='+list)