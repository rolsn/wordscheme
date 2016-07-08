from django.contrib.auth.models import User
from rest_framework import serializers

from website.models import Ratings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('user_id', 'art_id', 'rating')
