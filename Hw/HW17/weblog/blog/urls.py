from django.urls import path

from .views import *

urlpatterns = [
    path('all_post/', PostList.as_view(), name="post_list"),
    path('all_post/<slug:slug>/', post_detail, name='post_detail'),
    path('all_post/<int:pk>', CategoryDetail.as_view(), name='post-category'),
    path('post/', post_list, name='api_post_list'),
    path('post/<int:post_id>', post_details, name='api_post_details'),
    path('comment/', comment_list, name='api_comment_list'),
    path('comment/<int:id>', comment_details, name='api_comment_details'),
    path('tag/', tag_list, name='api_tag_list'),
    path('tag/<int:tag_id>', tag_details, name='api_tag_details'),
    path('category/', category_list, name='api_category_list'),
    path('category/<int:pk>', category_details, name='api_category_details'),
    path('hello/', HelloView.as_view(), name='hello'),

]
