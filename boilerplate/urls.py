from django.urls import path
from django.contrib import admin

from core import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
]
