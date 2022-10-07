from django.shortcuts import redirect

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shortener import services
from shortener import serializers
from shortener import permissions
from shortener import pagination


class UrlListAPIView(generics.ListAPIView):
    queryset = services.get_urls()
    serializer_class = serializers.UrlListSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = pagination.UrlPagination


class UrlUpdateAPIView(generics.UpdateAPIView):
    queryset = services.get_urls()
    serializer_class = serializers.UrlUpdateSerializer
    permission_classes = [permissions.IsOwnerOrAdminOrReadOnly, ]

    lookup_field = 'slug'


class UrlCreateAPIView(generics.CreateAPIView):
    queryset = services.get_urls()
    serializer_class = serializers.UrlSerializer
    permission_classes = [IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        """
        Overwrited create() method that generates unique slug for each new url
        and creates shorten_link from it
        :param request:
        :param args:
        :param kwargs:
        :return: response with shorten url
        """
        slug = services.generate_random_slug()
        shorten_link = f"{request.scheme}://{request.META['HTTP_HOST']}/r/{slug}"
        serializer = self.get_serializer(data={
            'url': self.request.data['url'],
            'shorten_link': shorten_link,
            'slug': slug,
            'user': self.request.user.pk
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "shorten_link": shorten_link,
            "message": "Shorten link created successfully",
        }, status=status.HTTP_201_CREATED, headers=headers)


class UrlRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = services.get_urls()
    serializer_class = serializers.UrlSerializer
    permission_classes = [permissions.IsOwnerOrAdminOrReadOnly, ]

    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        """
        Overwrited retrieve() method that redirects user from shorten link
        to destination url and increases visits_count on each redirect
        :param request:
        :param args:
        :param kwargs:
        :return: redirect instance
        """
        instance = self.get_object()
        instance.visits_count += 1
        instance.save()
        return redirect(instance.url)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Shorten link deleted successfully",
                         }, status=status.HTTP_202_ACCEPTED)
