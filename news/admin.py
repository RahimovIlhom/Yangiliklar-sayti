from django.contrib import admin
from .models import News
from comment.models import Comment

# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class NewsAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(News, NewsAdmin)
