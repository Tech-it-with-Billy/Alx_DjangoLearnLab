from django.db import models
from django.conf import settings
from datetime import datetime

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='actor', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f"{self.actor} {self.verb} {self.target if self.target else ''} at {self.timestamp}"

