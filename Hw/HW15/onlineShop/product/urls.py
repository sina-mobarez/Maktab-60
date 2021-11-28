from django.urls import path
from .views import *

urlpatterns = [
    path('today/', get_time_now),
    path('product/<int:index>', show_product_detail),
    path('product_detail/', show_product_template),

]
