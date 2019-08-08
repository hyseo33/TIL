from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10) #제한 글자수를 정해줌.
    content = models.TextField() #글자수 제한이 없다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'