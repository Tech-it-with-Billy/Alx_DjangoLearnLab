from django.urls import path, include
from .views import RegisterView, LoginView, UserProfileView, FollowUnfollowView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('follow/<str:username>/', FollowUnfollowView.as_view(), name='follow-unfollow'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('posts/', include('accounts.posts.urls')),
]