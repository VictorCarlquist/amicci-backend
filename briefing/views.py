from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Briefing, Vendor, Category, Retailer
from .serializers import BriefingSerializer, VendorSerializer, CategorySerializer, RetailerSerializer


class BriefingViewSet(viewsets.ModelViewSet):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer

