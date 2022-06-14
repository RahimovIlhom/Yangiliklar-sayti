from django.db import models
from django.urls import reverse
from category.models import Category
from django.contrib.auth import get_user_model

# Create your models here.

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news_image/')
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    blog_views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title