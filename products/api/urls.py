from django.urls import path

from .views import (
    list_of_cattegories,
    products
)

app_name = 'products'
urlpatterns = [
    path('categories/', list_of_cattegories, name="categories"),
    path('categories/<int:pk>', list_of_cattegories, name="category_detials"),
    path('products/', products, name="products")
]