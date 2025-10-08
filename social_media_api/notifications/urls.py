from django.urls import path
from .views import NotificationListView
from django.contrib.syndication.views import Feed

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('feed/', Feed(), name='notification-feed'),
]
