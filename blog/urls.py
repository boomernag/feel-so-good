from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('blog/', BlogListView, name='blog'),
    path('blog/<int:_id>', BlogDetailView, name='blog'),
]
