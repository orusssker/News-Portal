from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('news/<int:article_id>/', views.article_detail, name='article_detail'),
]
