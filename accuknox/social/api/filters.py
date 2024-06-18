from django_filters import FilterSet, CharFilter, NumberFilter, DateFilter
from django.db.models import Q
from django.contrib.auth import get_user_model


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