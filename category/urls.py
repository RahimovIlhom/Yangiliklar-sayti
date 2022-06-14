from django.urls import path
from .views import all_category, category

urlpatterns = [
   path('', all_category, name='all-category'),
   path('<int:id>', category, name='category'),
]
