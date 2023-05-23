from rest_framework import serializers
from .models import *


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrlHistory
        fields = ('original_url', 'converted_url', 'created_on')
