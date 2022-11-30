from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:post-detail")
    author = serializers.HyperlinkedRelatedField(view_name="api:user-detail", read_only=True)
    viewers = serializers.HyperlinkedRelatedField(view_name="api:user-detail", read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'url', 'author', 'viewers')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

