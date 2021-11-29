from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serilizers import *


# Create your views here.


# a class based view for show post's list and category' list
class PostList(ListView):
    context_object_name = 'post_list'
    template_name = "all_post.html"

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['category_post'] = Post.objects.filter(category__id=self.kwargs.get('pk'))
        return context


# a function based view for show detail of posts and show them comment under that      
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comment = Comment.objects.filter(post__slug=slug)
    category = Category.objects.all()
    return render(request, 'post_detail.html', {'post': post, 'comment': comment, 'category': category})


# a class based view for show post in a special category
class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['category_all'] = Category.objects.all()
        return context


@api_view(['GET'])
def post_list(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(post)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def comment_list(request):
    comment = Comment.objects.all()
    serializer = CommentSerializer(comment, many=True)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def comment_details(request, id):
    comment = get_object_or_404(Comment, id=id)
    serializer = CommentSerializer(comment)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def tag_list(request):
    tag = Tag.objects.all()
    serializer = TagSerializer(tag, many=True)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def tag_details(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    serializer = TagSerializer(tag)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def category_list(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def category_details(request, pk):
    category = get_object_or_404(Category, id=pk)
    serializer = CategorySerializer(category)
    return Response(data=serializer.data, status=200)
