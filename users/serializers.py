# -*- coding: utf-8 -*-
from rest_framework import serializers

__author__ = 'kas'


class UserSerializer(serializers.Serializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
