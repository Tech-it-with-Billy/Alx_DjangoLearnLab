from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, FollowUnfollowView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('follow/<int:user_id>/', FollowUnfollowView.as_view(), name='follow-unfollow-username'),
    path('follow/<int:user_id>/', FollowUnfollowView.as_view(), name='follow-unfollow-username'),
    path('/feed/', UserProfileView.as_view(), name='user-feed'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
]