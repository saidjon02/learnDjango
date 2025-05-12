from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # `myapp`ning URL'larini qo'shish
    path('myapp/', include('myapp.urls')),  # Bu yerda `myapp`ni sizning app nomingizga moslashtiring
]
