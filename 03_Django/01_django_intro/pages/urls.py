from django.urls import path
from . import views

urlpatterns = [ # 앱 url은 아래에서 추가
    path('static_ex/', views.static_ex),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('lotto/', views.lotto),
    path('ispal/<words>/', views.ispal),
    path('isbirth/', views.isbirth),
    path('template_language/', views.template_language),
    path('circle/<int:r>/', views.circle),
    path('multi/<int:num1>/<int:num2>/', views.multi),
    path('introduce2/<name>/<int:age>/', views.introduce2),
    path('hello/<name>/<int:age>/', views.hello),
    path('images/', views.images),
    path('index/', views.index),
    path('introduce/', views.introduce),
    path('dinner/', views.dinner),
]