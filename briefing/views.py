from django.shortcuts import render
from rest_framework import viewsets
from .models import Briefing, Vendor, Category, Retailer
from .serializers import BriefingSerializer, VendorSerializer, CategorySerializer, RetailerSerializer
from rest_framework.response import Response
from rest_framework import status


class BriefingViewSet(viewsets.ModelViewSet):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer

    def list(self, request, *args, **kwargs):
        list_obj = super().list(request, *args, **kwargs)
        if not list_obj.data:
            return Response(data="Não há briefing disponível", status=status.HTTP_404_NOT_FOUND)
        return list_obj


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def list(self, request, *args, **kwargs):
        list_obj = super().list(request, *args, **kwargs)
        if not list_obj.data:
            return Response(data="Não há vendor disponível", status=status.HTTP_404_NOT_FOUND)
        return list_obj


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer

    def list(self, request, *args, **kwargs):
        list_obj = super().list(request, *args, **kwargs)
        if not list_obj.data:
            return Response(data="Não há retailer disponível", status=status.HTTP_404_NOT_FOUND)
        return list_obj

