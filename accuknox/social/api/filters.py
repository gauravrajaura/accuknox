from django_filters import FilterSet, CharFilter
from django.db.models import Q
from django.contrib.auth import get_user_model

from accuknox.social.models import FriendRequest


User = get_user_model()


class UserFilterSet(FilterSet):
    search = CharFilter(method='filter_search_fields')
    
    class Meta:
        model = User
        fields = ['search']

    def filter_search_fields(self, queryset, name, value):
        if value:
            filter_conditions = Q()
            if "@" in value:
                return queryset.filter(email__iexact=value)

            fields_to_search = ['name'] # we can add 'email' too if we want
            for field in fields_to_search:
                filter_conditions |= Q(**{f'{field}__icontains': value})

            return queryset.filter(filter_conditions)
        return queryset
    

class FriendRequestFilterSet(FilterSet):
    query = CharFilter(method='filter_query')

    class Meta:
        model = FriendRequest
        fields = ['query']

    def filter_query(self, queryset, name, value):
        if value == 'pending-on-me':
            return queryset.filter(to_user=self.context.get('user'), status="pending")
        elif value == 'accepted-by-me':
            return queryset.filter(to_user=self.context.get('user'), status="accepted")
        elif value == 'pending':
            return queryset.filter(from_user=self.context.get('user'), status="pending")
        elif value == 'accepted':
            return queryset.filter(from_user=self.context.get('user'), status="accepted")
        elif value == 'friends':
            return queryset.filter(status="accepted")
    
    def __init__(self, *args, **kwargs):
        context = kwargs.pop('context', None)
        super().__init__(*args, **kwargs)
        self.context = context

