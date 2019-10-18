from django.contrib import admin
from .models import Article, Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)


# admin.site.register(Article, ArticleAdmin) 위에 @ 있는 한줄과 동일

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at', )

# admin.site.register(Comment, CommentAdmin)