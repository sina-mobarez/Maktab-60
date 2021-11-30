from .views import *
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static


urlpatterns = [
	path('all_post/', PostList.as_view(), name="post_list"),
	path('all_post/<slug:slug>/', post_detail, name='post_detail'),
	path('all_post/<int:pk>',CategoryDetail.as_view(), name= 'post-category'),
	
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
