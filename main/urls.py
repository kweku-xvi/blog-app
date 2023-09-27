from django.urls import path
from . import views
from .views import PostListView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='blog-create'),
]