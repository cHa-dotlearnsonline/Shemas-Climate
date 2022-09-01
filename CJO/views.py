from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms 
from .models import QuillPost
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
            savedPost = QuillPost(content=content2)
            savedPost.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors.as_data())
    material = QuillPost.objects.all()
    return render(request, "CJO/index.html", {
        "quill2": QuillPostForm2(),
        "mater": material 
    })


class QuillPostForm2(forms.Form):
    content1 = QuillFormField()