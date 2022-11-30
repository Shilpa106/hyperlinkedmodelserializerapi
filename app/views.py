from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny  # NOQA
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', ]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', ]

