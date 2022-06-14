from django.urls import path
from .views import news, detail

from . import views

urlpatterns = [
   path('', news, name='news'),
   path('<int:id>/detail', detail, name="detail"),
]
