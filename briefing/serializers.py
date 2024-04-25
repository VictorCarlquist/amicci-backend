from rest_framework import serializers
from .models import Briefing, Vendor, Category, Retailer


class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = '__all__'

