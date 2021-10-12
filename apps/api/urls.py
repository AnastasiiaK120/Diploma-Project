from django.urls import path
from .views import ProductApiView, DetailProduct

urlpatterns = [
    path('products', ProductApiView.as_view()),
    path('products/<int:pk>', DetailProduct.as_view()),
]