from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView
from .models import News
from category.models import Category
from comment.models import Comment
from accounts.models import CustomUser

# All News Page
def news(request):
    all_news = News.objects.all()
    return render(request, 'news.html', {
        'all_news': all_news
    })


class NewsDetailView(DetailView):

    model = News

    def get_object(self):
        obj = super().get_object()
        obj.blog_views += 1
        obj.save()
        return obj


# Deatil Page
def detail(request, id):
    news = News.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST['name']
        comment = request.POST['message']
        Comment.objects.create(
            news=news,
            name=name,
            comment=comment
        )
        messages.success(request, 'comment submitted but in moderation mode.')
    category = Category.objects.get(id=news.category.id)
    rel_news = News.objects.filter(category=category).exclude(id=id)
    comments = Comment.objects.filter(news=news).order_by('-id')
    return render(request, 'detail.html', {
        'news': news,
        'related_news': rel_news,
        'comments': comments
    })