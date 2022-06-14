from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)
    category_image = models.ImageField(upload_to='category_image/')
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title