from django.shortcuts import render
from .models import * 
from django.views.generic import TemplateView,ListView,DetailView
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
    post=Post.objects.get(slug=slug)
    comment = Comment.objects.filter(post__slug=slug)
    category = Category.objects.all()
    return render(request, 'post_detail.html', {'post':post , 'comment': comment , 'category': category})
    

# a class based view for show post in a special category
class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['category_all'] = Category.objects.all()
        return context
