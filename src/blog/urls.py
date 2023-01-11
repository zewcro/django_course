from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="blog-index"),
    path('article-<str:numero_article>/', article, name="blog-article"),
]
