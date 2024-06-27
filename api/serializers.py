from django.contrib.auth.models import Group, User
from rest_framework import serializers
from app import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'get_full_name']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['location','birthday']


class HubSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = models.Hub
        fields = ['name','slug']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Hub
        fields = '__all__'


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    hubs = HubSerializer(many=True)
    images = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = models.Activity
        fields = ['name', 'slug', 'body', 'user', 'hubs', 'images']