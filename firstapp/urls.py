from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('products',views.ProductListView.as_view(),name='product-list'),
    path('cuisinelist',views.Cuisine_list,name='Cuisine_list'),
    path('cuisineDetails/<int:pk>/',views.Cuisine_detail,name='Cuisine_Cuisine_detaillist'),

]