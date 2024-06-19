from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db.models import Q
from rest_framework import serializers

from accuknox.social.models import FriendRequest

User = get_user_model()


class UserRoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'last_login', 'date_joined']

class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = UserRoSerializer()
    to_user = UserRoSerializer()

    class Meta:
        model = FriendRequest
        fields = "__all__"


class CreateFriendRequestSerializer(serializers.ModelSerializer):
    to_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    class Meta:
        model = FriendRequest
        fields = ['to_user']

    def create(self, validated_data):
        from_user = self.context.get('request_user')
        to_user = validated_data.get('to_user')

        if from_user == to_user:
            raise serializers.ValidationError("You cannot send a friend request to yourself.")
        
        # Rate limit check using cache
        cache_key = f"friend_request_rate_{from_user.id}"
        request_count = cache.get(cache_key, 0)
        print("request_count",request_count)
        if request_count >= 3:
            raise serializers.ValidationError("You cannot send more than 3 friend requests within a minute.")
        cache.set(cache_key, request_count + 1, timeout=60)

        friend_request = FriendRequest.objects.filter(Q(to_user=from_user, from_user=to_user)|Q(from_user=from_user, to_user=to_user))
        if friend_request:
            raise serializers.ValidationError("This User has Already sent you the request.")
        friend_request = FriendRequest.objects.create(from_user=from_user, to_user=to_user)
        return friend_request
            
            
class UpdateFriendRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendRequest
        fields = ['status']


