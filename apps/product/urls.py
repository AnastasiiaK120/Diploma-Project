from django.urls import path

from . import views


from .views import ProductList, ProductDetail, UserDetail, UserList

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    path('products/', views.ProductDetail.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),

    path('<int:pk>/', ProductDetail.as_view()),
    path('', ProductList.as_view()),
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('<slug:category_slug>/', views.category, name='category'),
]



