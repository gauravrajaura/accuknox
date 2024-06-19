from django.conf import settings
from django.db import models
from django.utils import timezone

from accuknox.social.choices import FRIEND_REQUEST_STATUS

class FriendRequest(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_requests', on_delete=models.CASCADE, db_index=True)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_requests', on_delete=models.CASCADE, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.CharField(choices=FRIEND_REQUEST_STATUS, default="pending")

    class Meta:
        unique_together = ('from_user', 'to_user')

