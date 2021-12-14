import django_filters

from .models import Post


class PostListFilter(django_filters.FilterSet):
    category__title__icontains = django_filters.CharFilter(field_name='category__title', lookup_expr='icontains')
    created_at__year__gt = django_filters.NumberFilter(field_name='created_at', lookup_expr='year__gt')
    tag__lt = django_filters.NumberFilter(field_name='tag', lookup_expr='lt')
    tag__gt = django_filters.NumberFilter(field_name='tag', lookup_expr='gt')

    class Meta:
        model = Post
        fields = ['category__title__icontains', 'created_at__year__gt', 'tag__lt', 'tag__gt']

