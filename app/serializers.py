from rest_framework import serializers
import models
from django.contrib.auth.models import User

class post_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.post
		fields = ('id', 'body', 'time')
		
class authpost_old_serializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.PrimaryKeyRelatedField(
		read_only=True, allow_null=True, default='0')
	def validate_owner(self,value):
		return self.context['request'].user
		

	class Meta:
		model = models.authpost
		fields = ('id', 'owner', 'body', 'time')
		


class authpost_serializer(serializers.ModelSerializer):
	owner = serializers.PrimaryKeyRelatedField(
		source='owner.username', read_only=True, allow_null=True, default='0')
	def validate_owner(self,value):
		return self.context['request'].user

	class Meta:
		model = models.authpost
		fields = ('id', 'owner', 'body', 'time')
		
	def create(self, validated_data):
		validated_data['owner'] = self.context['request'].user
		return models.authpost.objects.create(**validated_data)
		
class comment_serializer(serializers.ModelSerializer):
	owner = serializers.PrimaryKeyRelatedField(
		source='owner.username', read_only=True, allow_null=True, default='0')
	def validate_owner(self,value):
		return self.context['request'].user

	class Meta:
		model = models.comment
		fields = ('id', 'owner', 'body', 'time','post')
		
	def create(self, validated_data):
		validated_data['owner'] = self.context['request'].user
		return models.comment.objects.create(**validated_data)
		
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username')
