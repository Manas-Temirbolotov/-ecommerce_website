from django.urls import path, include
from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryCreateAPIView.as_view(), name='category'),
    path('category/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_detail'),

    path('category/<int:pk>/item/', views.ItemCreateListApiView.as_view(), name='item'),
    path('category/<int:pk>/item/<int:id>/', views.ItemRetrieveUpdateDestroyApiView.as_view(), name='item_detail'),

    path('category/<int:pk>/item/<int:id>/order/', views.OrderCreateApiView.as_view(), name='order'),
    path('category/<int:pk>/item/<int:id>/order/<int:order_id>/'
         , views.OrderRetrieveUpdateDestroyApiView.as_view(), name='order_detail'),
]