from rest_framework.pagination import PageNumberPagination


class UrlPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 10