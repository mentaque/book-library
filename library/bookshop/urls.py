from django.urls import path
from bookshop.views import ProductsView, ProductItemView

urlpatterns = [
    path('', ProductsView.as_view(), name='shop_page'),
    path('<slug:product_id>/', ProductItemView.as_view(), name='product_item_page'),
]