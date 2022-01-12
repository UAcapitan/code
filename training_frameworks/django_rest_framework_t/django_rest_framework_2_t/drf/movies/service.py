from django_filters import rest_framework as filters
from movies.models import Movie, Review

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