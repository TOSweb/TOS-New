from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *
from . import views 


urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus/', views.about, name='about'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)