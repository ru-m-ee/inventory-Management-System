from django.urls import path
from customer_app import views

urlpatterns = [
    path('customer/', views.api_list),
    path('customerdetails/<int:pk>/', views.api_detail),
]