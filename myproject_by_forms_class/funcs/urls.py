from django.conf.urls import url
from . import views
from .views import homePageView
from django.urls import path

urlpatterns = [
    path(r'demo/', views.demoView, name='demo'),
    path(r'', homePageView, name='home'),    
]