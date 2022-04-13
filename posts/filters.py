from django_filters.rest_framework import FilterSet, DateTimeFilter

from .models import Like


class LikesFilter(FilterSet):
    date_from = DateTimeFilter(field_name='liked_date',
                                             lookup_expr='gte')
    date_to = DateTimeFilter(field_name='liked_date',
                                           lookup_expr='lte')

    class Meta:
        model = Like
        fields = ['date_from', 'date_to']