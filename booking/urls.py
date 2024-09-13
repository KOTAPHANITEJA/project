from django.urls import path 
from . import views 
urlpatterns=[ 
    path('', views.home, name='home'),
    path('hotel_list/', views.hotel_list, name='hotel_list'),
    path('movie_list', views.movie_list, name='movie_list'),
    path('restaurant_list', views.restaurant_list, name='restaurant_list'),
]