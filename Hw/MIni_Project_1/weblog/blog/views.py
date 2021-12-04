from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *


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


def add_post(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = 'admin'
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'add_post.html', {'form': form, 'category': category})


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('post_list')
    else:
        form = UserCreateForm()
    return render(request, 'registration/signup.html', {'form': form})


def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['mubarriizz@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
    return render(request, 'contact.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    user = request.user
    posts = Post.objects.filter(posted_by=user)
    category = Category.objects.all()
    return render(request, 'dashboard.html', {'posts': posts, 'user': user, 'category': category})
