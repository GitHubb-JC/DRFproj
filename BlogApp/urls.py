from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
# ViewSet 을 사용하면서 view 는 사용 높
# from .views import PostList, PostDetail, UserList, UserDetail
from .views import PostViewSet, UserViewSet
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# Router 생성
router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # 이를 통해 API URL 은 Router에 의해 자동적으로 결정!
]

#################################################################

# ## ViewSet 을 이용한 url
# # url요청시 작동될 view를 지정해주자
# # ViewSet 클래스의 뷰들을 HTTP 메서드에 따라 실제 뷰와 연결
# # 각 HTTP 메서드마다 작동될 기능(list, create 등등) 지정
# post_list = PostViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })

# post_detail = PostViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partail_update',
#     'delete': 'destroy',
# })

# user_list = UserViewSet.as_view({
#     'get': 'list',
# })

# user_detail = UserViewSet.as_view({
#     'get': 'retrieve',
# })

# urlpatterns = [
#     path('posts/', post_list, name='post_list'),
#     path('posts/<int:pk>/', post_detail, name='post_detail'),
#     path('user/', user_list, name='user_list'),
#     path('user/<int:pk>/', user_detail, name='user_detail'),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

#############################################################

## ViewSet 사용전 url들
# urlpatterns = [
#     path('posts/', PostList.as_view(), name='post_list'),
#     path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),

#     path('user/', UserList.as_view()),
#     path('user/<int:pk>/', UserDetail.as_view()),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)