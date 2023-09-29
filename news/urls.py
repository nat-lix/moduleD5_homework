from django.contrib import admin
from django.urls import path
from .views import PostList, PostDetail, Posts, SearchView, PostCreate, PostUpdateView, PostDeleteView

app_name = 'news'
urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/', Posts.as_view(), name='posts'),
    path('search/', SearchView.as_view(), name='post_search'),
    path('create_post/', PostCreate.as_view(), name='post_create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    
]
