from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreateFrom

class SignUpView(CreateView):
    form_class = CustomUserCreateFrom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'