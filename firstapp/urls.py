from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('cuisinelist',views.Cuisine_list,name='Cuisine_list'),
    path('cuisineDetails/<int:pk>/',views.Cuisine_detail,name='Cuisine_Cuisine_detaillist'),

]