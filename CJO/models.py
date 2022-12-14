from django.db import models
from django_quill.fields import QuillField
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=255)


class NewsArticle(models.Model):
    leadImage = models.ImageField(upload_to='files/leadImages')
    description= models.TextField(blank=True)
    headLine = models.CharField(max_length=300)
    content = QuillField()
    timestamp= models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete = models.PROTECT)

