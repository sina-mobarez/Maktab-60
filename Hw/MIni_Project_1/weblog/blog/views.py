from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.template.defaultfilters import title
from django.urls.base import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
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
    cm_count = Comment.objects.filter(post__id=post.id).count()
    likes = post.total_likes()
    tags = Tag.objects.filter(post__id=post.id)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cm = form.save(commit=False)
            cm.post = post
            cm.name = request.user
            cm.save()
            

            return redirect('post_detail', slug= slug) 
    return render(request, 'post_detail.html', {'post': post, 'comment': comment, 'category': category, 'form': form, 'total_likes': likes, 'liked': liked, 'comment_count': cm_count, 'tags': tags})


# a class based view for show post in a special category
class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['category_all'] = Category.objects.all()
        return context

class TagDetail(DetailView):
    model = Tag
    context_object_name = 'tag'
    template_name = "tag.html"

    def get_context_data(self, **kwargs):
        context = super(TagDetail, self).get_context_data(**kwargs)
        context['tag_all'] = Tag.objects.all()
        return context




def add_post(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = request.user
            post.save()
            form.save_m2m()
            return redirect('dashboard')
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
            subject = f'{form.cleaned_data["subject"]} ; Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['mubarriizz@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, 'Success, Your email has been sent', 'success')
            return redirect('post_list')
    return render(request, 'contact.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    user = request.user
    posts = Post.objects.filter(posted_by=user)
    category = Category.objects.all()
    return render(request, 'dashboard.html', {'posts': posts, 'user': user, 'category': category})


# don't save image
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = request.user
            post.modified = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})



class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name= 'registration/password_change_form.html'


def search(request):
    category = Category.objects.all()
    if request.method == 'POST':
        searched = request.POST['searched']
        post = Post.objects.filter(title__contains=searched)
        posts = Post.objects.filter(bodytext__contains=searched)

        return render(request, 'search.html', {'searched': searched, 'posts': post, 'category': category, 'postss': posts})
    else:
        return render(request, 'search.html', {})   


def LikeView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post_detail', args=[str(slug)]))


def add_category_tag(request):
    category_form = CategoryForm()
    tag_form = TagForm()
    category = Category.objects.all() 
    tag = Tag.objects.all()
    if request.method == "POST":
        print(request.POST)
        if request.POST['forcefield'] == 'c':    
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                return redirect('add-cat-tag')
        elif request.POST['forcefield'] == 't':
            tag_form = TagForm(request.POST)
            if tag_form.is_valid():
                tag_form.save()
                return redirect('add-cat-tag')
    else:
        tag_form = TagForm()
        category_form = CategoryForm()
    return render(request, 'add-cat-tag.html', {'tags': tag, 'category': category,'catform': category_form, 'tagform': tag_form})


def delete_c(request,id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.delete()
        return redirect(reverse('add-cat-tag'))

    return render(request,'delete-c.html',{'category':category})


def delete_t(request,id):
    tag = get_object_or_404(Tag, id=id)
    if request.method == "POST":
        tag.delete()
        return redirect(reverse('add-cat-tag'))

    return render(request,'delete-t.html',{'tag':tag})


def edit_t(request,id):
    tag = get_object_or_404(Tag,id=id)
    if request.method == "POST":
        form =TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect(reverse('add-cat-tag'))
    else:
        form = TagForm(instance=tag)
    return render(request,'edit-t.html',{'form':form,'tag':tag})


def edit_c(request,id):
    category = get_object_or_404(Category,id=id)
    if request.method == "POST":
        form =CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect(reverse('add-cat-tag'))
    else:
        form = CategoryForm(instance=category)
    return render(request,'edit-c.html',{'form':form,'category':category})


def delete_post(request,slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect(reverse('dashboard'))

    return render(request,'delete-post.html',{'post':post})