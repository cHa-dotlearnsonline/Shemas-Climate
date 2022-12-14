from django.urls import path 
from django.contrib import admin
from . import views 
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.index, name="index"),
    path("news", views.news, name="news"),
    path("news/<int:article_id>", views.articles, name="articles")
]

# To allow to serve static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)