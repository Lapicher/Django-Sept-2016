# -*- coding: utf-8 -*-
from rest_framework import serializers

from photos.models import Photo

__author__ = 'kas'


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo