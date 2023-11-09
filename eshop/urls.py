from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contactUs'),
    path('tracker/', views.tracker, name='track'),
    path('search/', views.search, name='Search'),
    # path('productView/', views.product_view, name='productView'),
    # products is a variable that is comes from views.py
    path('products/<int:myid>', views.product_view, name='productView'),
    path('checkOut/', views.checkOut, name='checkOut'),
    path('practice/', views.practice, name='practice'),
]
