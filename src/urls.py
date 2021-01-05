from django.urls import path
from django.contrib import admin

import src.core.views

urlpatterns = [
    path('', src.core.views.home),
    path('admin/', admin.site.urls),
]
