from django.urls import path
from .views import PostViewSet, CommentViewSet, UserFeedsViewSet, LikeViewSet, UnLikeViewSet
from rest_framework.authtoken.views import obtain_auth_token

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('posts/', post_list, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('comments/', comment_list, name='comment-list'),
    path('comments/<int:pk>/', comment_detail, name='comment-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('posts/<int:pk>/like/', LikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='like-list'),
    path('posts/<int:pk>/unlike/', UnLikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='unlike-list'),
    path('feed/', UserFeedsViewSet.as_view({'get': 'list'}), name='user-feed'),
]

            