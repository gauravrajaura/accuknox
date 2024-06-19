from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
)
from rest_framework import generics, pagination, viewsets
from rest_framework.exceptions import NotFound

from accuknox.social.api.filters import FriendRequestFilterSet, UserFilterSet
from accuknox.social.api.serializers import (
    CreateFriendRequestSerializer, 
    FriendRequestSerializer, 
    UpdateFriendRequestSerializer, 
    UserRoSerializer
)
from accuknox.social.models import FriendRequest


User = get_user_model()

class UserSearchView(generics.ListAPIView):
    serializer_class = UserRoSerializer
    pagination_class = pagination.PageNumberPagination
    queryset = User.objects.filter(is_active=True)

    def get_queryset(self):
        users_queryset = UserFilterSet(
            self.request.query_params, 
            queryset=self.queryset
        ).qs
        return users_queryset.order_by('id')


class FriendRequestView(
    viewsets.GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
):
    def get_queryset(self, **kwargs):
        queryset = FriendRequest.objects.filter(
            Q(from_user=self.request.user)|
            Q(to_user=self.request.user)
        ).select_related('from_user', 'to_user').order_by("-timestamp")
        
        filtered_queryset = FriendRequestFilterSet(
            self.request.query_params, 
            queryset=queryset,
            context={'user': self.request.user}
        ).qs        
        return filtered_queryset

    def get_object(self, **kwargs):
        if self.request.method == "DELETE":
            query = Q(from_user=self.request.user)
        else :
            query = Q(to_user=self.request.user)
        try:
            friend_request = FriendRequest.objects.get(query, id=self.kwargs.get('pk'))
            return friend_request
        except FriendRequest.DoesNotExist:
            raise NotFound(f"FriendRequest with pk {self.kwargs.get('pk')} not found or FriendRequest is not associated with you")    

    def get_serializer_context(self):
        context = super(self.__class__, self).get_serializer_context()
        context.update({"request_user": self.request.user,})
        return context

    def get_serializer_class(self):
        if self.request.method == "GET" or self.request.method == "DELETE":
            return FriendRequestSerializer
        elif self.request.method == "POST":
            return CreateFriendRequestSerializer
        elif self.request.method == "PATCH":
            return UpdateFriendRequestSerializer
