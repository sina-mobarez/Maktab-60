from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post, User
from .serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(published=True)
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data, status=200)
    elif request.method == 'POST':
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
        return Response(data=serializer.data, status=200)
        
@api_view(['GET'])
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serializer = PostDetailSerializer(post)
    return Response(data=serializer.data, status=200)