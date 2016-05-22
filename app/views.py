import models
from rest_framework import viewsets, generics
import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from app.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet that for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.filter(username = request.user.username)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
class post(viewsets.ModelViewSet):
	serializer_class = serializers.post_serializer
	queryset = models.post.objects.all()
	
class authpost(viewsets.ModelViewSet):
	serializer_class = serializers.authpost_serializer
	queryset = models.authpost.objects.all().order_by("id").reverse()

class fetch(viewsets.ModelViewSet):
	serializer_class = serializers.authpost_serializer
	def get_queryset(self):
		uname = self.kwargs['name']
		user_id = User.objects.get(username=uname).id
		return models.authpost.objects.filter(owner=user_id).order_by("id").reverse()
		
class fetch_id(viewsets.ModelViewSet):
	serializer_class = serializers.authpost_serializer
	def get_queryset(self):
		identification = self.kwargs['post_id']
		return models.authpost.objects.filter(id=identification)

class fetch_com(viewsets.ModelViewSet):
	serializer_class = serializers.comment_serializer
	def get_queryset(self):
		user_id = self.kwargs['identification']
		return models.comment.objects.filter(post=user_id).order_by("id")

class comment(viewsets.ModelViewSet):
	serializer_class = serializers.comment_serializer
	queryset = models.comment.objects.all().order_by("id")

"""
class current_user(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	def get_queryset(self, request):
		return = UserSerializer(request.user)
"""
