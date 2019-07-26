from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('product/<int:pk>/',views.ProductDetailView.as_view(),name="product_view"),
    path('cart/',views.CartView.as_view(),name="cart"),
    path('cart/<int:pk>/remove/',views.CartRemoveView.as_view(),name='cart_remove'),
    path('seller/',views.CreateSeller.as_view(),name='create-seller'),
    path('buyer/',views.CreateBuyer.as_view(),name='create-buyer'),
    path('newproduct/',views.ProductCreate.as_view(),name='create-product'),
    path('edit/<int:pk>/',views.ProductEditView.as_view(),name='edit-product'),
    path('product/category/',views.CategorySearchView.as_view(),name='category-view'),
    path('product/<int:pk>/review/',views.ReviewView.as_view(),name='review-view'),
    path('checkout/',views.CheckOutView.as_view(),name='checkout'),
    path('pay',views.pay,name='pay'),
    path('delete/<int:pk>/',views.ProductDeleteView.as_view(),name='delete')
]
