#authentication/urls.py
from django.contrib.auth.decorators import login_required
from .views import register, user_login, user_logout, user_profile, dashboard
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'userAuthentication'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', login_required(user_profile), name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', user_profile, name='user_profile'),
    path('logout/', user_logout, name='logout'),
]

