from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import stringfilter

from .models import News, Article

def news_list(request):
    news_list = News.objects.order_by('-publication_date')
    return render(request, 'news_list.html', {'news_list': news_list})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article_detail.html', {'article': article})

@stringfilter
def censor(value):
    unwanted_words = ['нежелательное1', 'нежелательное2', 'нежелательное3']
    for word in unwanted_words:
        value = value.replace(word, '*' * len(word))
    return value
