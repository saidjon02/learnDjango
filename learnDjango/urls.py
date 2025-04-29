# your_project/urls.py
from django.urls import path
from myapp import views
from django.contrib import admin

urlpatterns = [
    path('', views.signup, name='signup'),
    path('admin/', admin.site.urls),
   path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]

