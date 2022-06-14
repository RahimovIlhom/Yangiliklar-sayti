from django.shortcuts import render
from .models import Category
from news.models import News

# fetch all category
def all_category(request):
    cats = Category.objects.all()
    return render(request, 'category.html', {
        'cats': cats
    })


# fetch news in category
def category(request, id):
    cat = Category.objects.get(id=id)
    news = News.objects.filter(category=cat)
    return render(request, 'category-news.html', {
        'all_news': news,
        'category': cat
    })