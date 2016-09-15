# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView

from photos.models import Photo
from photos.serializers import PhotoSerializer

__author__ = 'kas'


class PhotoListAPI(ListCreateAPIView):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer