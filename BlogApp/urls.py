from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostList, PostDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)