from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('post_list/', views.post_list, name='post_list'),  # Postlar ro'yxati
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
