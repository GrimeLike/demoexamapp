from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('', main_page),
    path('signup/', SignUpView.as_view()),
    path('catalog/', product_list, name='product_list'),
    path('catalog/<str:category_slug>/', product_list, name='product_list_by_category'),
    path('catalog/<int:id>/<str:slug>/', product_detail, name='product_detail'),
    path('about/', about),
    path('contact/', contact),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('orders/create/', order_create, name='order_create'),
    path('coupons/apply/', coupon_apply, name='apply')
]
