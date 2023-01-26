from django.urls import path 
from . import views


urlpatterns = [
    path('load/', views.GetData.as_view(), name='load'),
    path('', views.listing, name='index')
]