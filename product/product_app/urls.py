from django.urls import path
from product_app import views

urlpatterns = [
    path('product/', views.p_list),
    path('productdetails/<int:pk>/', views.p_detail),
    
]