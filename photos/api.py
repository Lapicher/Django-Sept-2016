# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer

__author__ = 'kas'


class PhotoListAPI(ListCreateAPIView):
    """
    Endpoint de listado y creación de fotos
    """
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer


class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualización y borrado de fotos
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
