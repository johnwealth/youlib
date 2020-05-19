
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('library/', views.resource, name= 'resource'),
    path('trending/', views.trending, name= 'trending'),
    path('category/', views.category, name= 'category'),
    path('explore/', views.category, name= 'explore'),
    path('live/', views.live, name= 'live'),

]
