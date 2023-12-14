# marketplace/urls.py
from django.urls import path
from .views import sell_item
from .views import my_posts

app_name = 'marketplace'

urlpatterns = [
    path('sell-item/', sell_item, name='sell_item'),
    path('my-posts/', my_posts, name='my_posts'),
]