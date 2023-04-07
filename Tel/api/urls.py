from django.urls import path
from .views import *

urlpatterns = [
    path('cats/', CategoryCreateListView.as_view(), name="cats"),
    path('cat/<int:pk>/', CategoryRetrieveUpdateDestroyApiView.as_view(), name="cat_change"),
    path('brands/', BrandCreateListView.as_view(), name="brands"),
    path('brand/<int:pk>/', BrandRetrieveUpdateDestroyApiView.as_view(), name="brand_change"),
    path('products/', ProductCreateListView.as_view(), name="products"),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyApiView.as_view(), name="product_change")
]   