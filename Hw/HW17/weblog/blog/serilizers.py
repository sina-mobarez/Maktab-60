from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    posted_by = UserSerializer(read_only=True)
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['title', 'slug', 'bodytext', 'category', 'posted_by', 'tag']


class CommentSerializer(serializers.ModelSerializer):
    name = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = ['name', 'email', 'post', 'body', 'created']

