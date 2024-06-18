from rest_framework import generics, pagination
from django.contrib.auth import get_user_model

from accuknox.social.api.filters import UserFilterSet
from accuknox.social.api.serializers import UserRoSerializer


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

