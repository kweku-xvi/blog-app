from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostCreateView, 
    # PostDetailView, 
    PostUpdateView, 
    PostDeleteView,
    UserPostsListView
    )

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>/detail/', views.post_detail, name='blog-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
    path('user/<str:username>/', UserPostsListView.as_view(), name='user-posts'),
]