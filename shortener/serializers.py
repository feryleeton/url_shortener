from rest_framework import serializers
from shortener import models


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Url
        fields = [
            'url',
            'slug',
            'shorten_link',
            'visits_count',
            'user',
        ]


class UrlUpdateSerializer(serializers.ModelSerializer):
    """
    UrlUpdate serializer with defined read_only_fields to except some data from updating
    """

    class Meta:
        model = models.Url
        fields = [
            'slug',
            'shorten_link',
            'visits_count',
            'url',
        ]
        read_only_fields = [
            'slug',
            'shorten_link',
            'visits_count',
            'user',
        ]


class UrlListSerializer(serializers.Serializer):
    """
    Custom UrlList serializer with overwrited to_representation()
    method to display visits_count value only for owners and admins
    """

    def to_representation(self, value):
        request = self.context['request']
        url = models.Url.objects.get(slug=value.slug)
        if request.user == url.user or request.user.is_staff:
            return {
                'url': url.url,
                'shorten_link': url.shorten_link,
                'visits_count': url.visits_count,
            }
        else:
            return {
                'url': url.url,
                'shorten_link': url.shorten_link,
            }

