from .views import *
from django.urls import path
from django.urls import path

from .views import *

urlpatterns = [
    path('all_post/', PostList.as_view(), name="post_list"),
    path('all_post/<slug:slug>/', post_detail, name='post_detail'),
    path('all_post/<int:pk>', CategoryDetail.as_view(), name='post-category'),
    path('add_post/', add_post, name='add_post'),
    path('contact/', contact_form, name='contact'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
]
