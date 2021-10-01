from django.urls import path

from . import views

from .views import ProductList, ProductDetail

urlpatterns = [
    path('<int:pk>/', ProductDetail.as_view()),
    path('', ProductList.as_view()),
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('<slug:category_slug>/', views.category, name='category'),
]