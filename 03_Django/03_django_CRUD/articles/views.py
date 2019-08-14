from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()[::-1]
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

    #CREATE

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect(f'/articles/{article.pk}/')

    #READ

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)

    #DELETE

def delete(request, pk): #POST요청은 무조건 redirect 시켜야함.
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('/articles/')

    #UPDATE

def edit(request, pk):
    article = Article.objects.get(pk=pk) #DB에서 가져오기
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    
    return redirect(f'/articles/{article.pk}/')
