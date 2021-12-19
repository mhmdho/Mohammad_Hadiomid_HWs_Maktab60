from django.db.models import fields
from django.db.models.aggregates import Count
import django_filters
from django_filters import filters

from .models import Post


# Doc Way:
# class PostListFilter(django_filters.FilterSet):
    
#     tags_count = django_filters.NumberFilter()
#     tags_count__gt = django_filters.NumberFilter(field_name='tags_count', lookup_expr='gt')
#     tags_count__lt = django_filters.NumberFilter(field_name='tags_count', lookup_expr='lt')

#     created_year = django_filters.NumberFilter(field_name='created', lookup_expr='year')
#     created_year__gt = django_filters.NumberFilter(field_name='created', lookup_expr='year__gt')
#     created_year__lt = django_filters.NumberFilter(field_name='created', lookup_expr='year__lt')

#     manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')
   
#     class Meta:
#         model = Post
#         fields = ['tag', 'tags_count', 'created']



class PostListFilter(django_filters.FilterSet):
    # First Way:
    tags_count = django_filters.NumberFilter(method='filter_tags_count') # not working!
    class Meta:
        model = Post
        fields = {
            'created': ['year__lt', 'year__gt'],
            'tag': ['exact', 'lt'],
        }

    def filter_tags_count(self,queryset, key, value):
        queryset = queryset.annotate(tcount=Count('tags')).filter(tcount=value)
        return queryset


    # Second Way:
    # tag = django_filters.NumberFilter(fields='tag', lookup_expr=['exact', 'lt'])
    # class Meta:
    #     model = Post
    #     fields = ['tags_count', 'tag', 'created']
        
    # def filter_tags_count(self,queryset, key, value):
    #     queryset = queryset.annotate(tcount=Count('tags')).filter(tcount=value)
    #     return queryset
