from django.shortcuts import render
from news.models import News
from category.models import Category

#  Home Page
def homePageView(request):
    first_news = News.objects.last()
    three_news = News.objects.all()[0:4]
    three_categories = Category.objects.all()[0:4]

    return render(request, 'home.html', {
        'first_news': first_news,
        'three_news': three_news,
        'three_categories': three_categories,
        }
    )