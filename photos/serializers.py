# -*- coding: utf-8 -*-
from rest_framework import serializers

from photos.models import Photo

__author__ = 'kas'


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo


class PhotoListSerializer(PhotoSerializer):

    class Meta(PhotoSerializer.Meta):
        fields = ("id", "name", "url")
