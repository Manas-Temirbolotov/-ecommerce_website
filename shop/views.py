from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework import status, authentication
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from .mixins import DetailGetPutPostMixin
from .models import Category, Item, Order
from .permissions import IsAuthorPermission, IsSenderReadOnly, IsBuyerReadOnly
from .serializers import CategorySerializer, ItemSerializer, OrderSerializer
from .views_generic import ModelGetPostView


class CategoryCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication, SessionAuthentication]

    permission_classes = [IsSenderReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthorPermission, ]


class ItemCreateListApiView(ListCreateAPIView):
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsSenderReadOnly, ]

    def get_queryset(self):
        category = self.kwargs['pk']
        return Item.objects.filter(category=category)

    def perform_create(self, serializer):
        category = Category.objects.filter(pk=self.kwargs['pk']).first()
        serializer.save(category=category)
        serializer.save(profile=self.request.user)


class ItemRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, ]

# class ModelGetPostView:
#     pass


class OrderCreateApiView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsBuyerReadOnly, ]


class OrderRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsBuyerReadOnly, ]
