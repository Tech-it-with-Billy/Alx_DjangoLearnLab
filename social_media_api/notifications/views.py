from django.shortcuts import render
from .models import Notification
from django.views import generic

# Create your views here.
class NotificationListView(generic.ListView):
    model = Notification
    template_name = 'notifications/notification_list.html'
    context_object_name = 'notifications'
    paginate_by = 10

    def get_queryset(self):
        return Notification.objects.all().order_by('-timestamp')
