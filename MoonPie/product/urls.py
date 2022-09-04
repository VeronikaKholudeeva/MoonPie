
from django.urls import path, include

from product import views

urlpatterns = [
    path('getProduct/', views.getProduct.as_view()),
    path('gethotProduct/', views.gethotProduct.as_view()),
    path('getReview/', views.getReview.as_view()),
    path('getFilter/', views.filterbybase),
    path('getLastReview/', views.getLastReview.as_view()),
    path('products/search/', views.search),
    path('products/<slug:taste_slug>/<slug:base_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('checkout/', views.checkout),
    path('orders/', views.OrderList.as_view())
]