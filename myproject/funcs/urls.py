from django.conf.urls import url
from . import views
from .views import homePageView
from django.urls import path

urlpatterns = [
    path(r'demo/', views.index, name='index'),
    path(r'', homePageView, name='home'),    
]