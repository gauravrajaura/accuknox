from django.conf import settings
from django.db import models
from django.utils import timezone

class FriendRequest(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_requests', on_delete=models.CASCADE, db_index=True)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_requests', on_delete=models.CASCADE, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('from_user', 'to_user')

class Friendship(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friends1', on_delete=models.CASCADE, db_index=True)
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friends2', on_delete=models.CASCADE, db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ('user1', 'user2')

class FriendRequestRateLimit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
