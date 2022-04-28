from django_filters import rest_framework as filters
from movies.models import Movie, Review
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict

class MovieAllFilter(filters.FilterSet):
    id = filters.RangeFilter()

    class Meta():
        model = Movie
        fields = ['id',]

class ReviewFilter(filters.FilterSet):
    id = filters.RangeFilter()

    class Meta():
        model = Review
        fields = ['id',]

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class MovieFilter(filters.FilterSet):
    id = filters.RangeFilter()
    id_of_movie = CharFilterInFilter(field_name='id_of_movie')

    class Meta():
        model = Movie
        fields = ['id','id_of_movie']

class PaginationMovies(PageNumberPagination):
    page_size = 2
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(
            {
                'count': self.page.paginator.count,
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link(),
                },
                'results': data,
            }
        )