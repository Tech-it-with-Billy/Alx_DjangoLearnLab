from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth import login, logout
from django.urls import path

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

urlpatterns = [
    path('login/', login, name='login'),
]

urlpatterns = [
    path('logout/', logout, name='logout'),
]


