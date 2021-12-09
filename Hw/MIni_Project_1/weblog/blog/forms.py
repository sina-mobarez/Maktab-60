from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import fields


from .models import *

class CategoryForm(forms.ModelForm):
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput(attrs={'value': 'c'}), label="Leave empty")

    class Meta:
        model = Category
        fields = '__all__'


class TagForm(forms.ModelForm):
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput(attrs={'value': 't'}), label="Leave empty")

    class Meta:
        model = Tag
        fields = '__all__'



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'bodytext', 'pic', 'category', 'tag', 'status')
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'body')


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'exists': 'This email already exists!'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']


def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=80)
    subject = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput, label="Leave empty", validators=[should_be_empty])


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length= 100 ,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(max_length= 100 ,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(max_length= 100 ,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_active','email')
