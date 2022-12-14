from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms 
from .models import NewsArticle, Category
from django.urls import reverse
from django_quill.forms import QuillFormField
# Create your views here.

def index(request):

    if request.method == "POST":
        form = QuillPostForm2(request.POST)
        print("This is a POST request")
        if form.is_valid():
            #print("The form is valid")
            content2 = form.cleaned_data["content1"]
            savedPost = NewsArticle(content=content2)
            savedPost.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors.as_data())
    material = NewsArticle.objects.all()[:3]
    return render(request, "CJO/index.html", {
        "quill2": QuillPostForm2(),
        "mater": material 
    })


def news(request):
    news_content = NewsArticle.objects.all()
    categories = Category.objects.all()

    news_by_category = []

    for category in categories:
        articles = NewsArticle.objects.filter(category = category)
        # to arrange in reverse chronological order
        articles = articles.order_by("-timestamp").all()
        news_by_category.append(articles)

    return render(request, "CJO/news.html", {
        "articles": news_by_category
        })

def articles(request, article_id):

    article = NewsArticle.objects.get(id=article_id)


    return render(request, "CJO/article.html", {
        "quill2": QuillPostForm2(),
        "article": article 
        })



class QuillPostForm2(forms.Form):
    content1 = QuillFormField()



