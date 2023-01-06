from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostList, PostDetail, UserList, UserDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),

    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)