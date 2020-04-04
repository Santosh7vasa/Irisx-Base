from django.urls import path, include
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    LanguageView,
    UserPostListView)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', LanguageView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('rest', include(router.urls)),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about', views.about, name='blog-about')
]