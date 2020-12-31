from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:post_title>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_title>/', views.delete_post, name='delete_post'),
]
