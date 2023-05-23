from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response

import string
from random import choice

from .models import UrlHistory
from .serializers import UrlSerializer


class UrlConverterView(ListAPIView, CreateAPIView):
    serializer_class = UrlSerializer
    model = UrlHistory
    lookup_url_kwarg = 'original_url'

    def get_queryset(self):
        queryset = UrlHistory.objects.all()
        url_param = self.request.query_params.get('converted_url')

        if url_param is not None:
            converted_url = "http://localhost:8000/short_url/?converted_url=" + url_param
            queryset = queryset.filter(converted_url=converted_url)
            return queryset

        return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        original_url = request.data["original_url"]

        url_object = UrlHistory.objects.filter(original_url=original_url).first()

        """ do need to create new one if url already exists"""
        if url_object:
            return Response(data={"original_url": url_object.original_url,
                                  "converted_url": url_object.converted_url}, status=status.HTTP_200_OK)

        num_of_chars = 8
        last_row_id = ''
        if UrlHistory.objects.count() > 0:
            last_row_id = str(UrlHistory.objects.latest('id').id)

        short_id = last_row_id + ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_of_chars))
        converted_url = "http://localhost:8000/short_url/?converted_url=" + short_id
        serializer = UrlSerializer(data={"original_url": original_url, "converted_url": converted_url})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
