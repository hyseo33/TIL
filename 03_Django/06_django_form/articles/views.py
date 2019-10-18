from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    """
    1. Form Class
    모델에 대한 정보를 알지 못해서 유효성 검사 이후에 cleaned_data를 통해 data 정제 후
    db에 저장하는 로직 필요

    2. Model Form
    이미 모델에 대한 정보(스키마)를 알고 있기 때문에 어떤 모델에 레코드를 넣어야 하는지 알고 있음
    form.save()만 해도 db에 저장됨
    """
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채운다.
        form = ArticleForm(request.POST)
        # 해당 form이 유효한지 확인
        if form.is_valid():
            article = form.save()
            # embed()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        # embed()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)

# def create(request):
#     if request.method == 'POST':
#         # form 인스턴스를 생성하고 요청에 의한 데이터로 채운다.
#         form = ArticleForm(request.POST)
#         # 해당 form이 유효한지 확인
#         if form.is_valid():
#             # form.cleaned_data를 통해 form 데이터를 정제힌다.(form.cleaned_data -> Dict))
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             article = Article.objects.create(title=title, content=content)
#             # embed()
#             return redirect('articles:detail', article.pk)
#     else:
#         form = ArticleForm()
#         # embed()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index') # redirect -> GET 요청

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # instance -> 수정의 대상이 되는 특정한 글 객체
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            # embed()
            return redirect('articles:detail', article_pk)
    else:
        form = ArticleForm(instance=article)
        # form = ArticleForm(initial=article.__dict__)
        # embed()
    context = {
        'form': form,
        'article': article,
    }
    # embed()
    return render(request, 'articles/form.html', context)

"""
* CREATE & UPDATE는 동일 html 파일 공유
Create 로직
1.GET
- 사용자가 데이터를 입력할 수 있는 빈 form을 제공
2.POST
- 사용자가 보낸 새로운 글을 DB에 저장

Update 로직
1.GET
- 사용자의 기존 글이 입력된 form 제공
2.POST
- 수정된 글을 DB에 저장
"""

@require_POST
def comments_create(request, article_pk):
    # article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
    