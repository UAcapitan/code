from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict

class PaginationArticle(PageNumberPagination):
    page_size = 3
    max_page_size = 1000

class PagonationArticlePageSize10(PageNumberPagination):
    page_size = 10
    max_page_size = 1000