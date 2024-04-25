from rest_framework import serializers
from .models import Briefing, Vendor, Category, Retailer


class RetailerField(serializers.Field):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return Retailer.objects.get(pk=data)

class CategoryField(serializers.Field):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return Category.objects.get(pk=data)


class BriefingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Briefing
        fields = '__all__'

    retailer = RetailerField()
    category = CategoryField()


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RetailerSerializer(serializers.ModelSerializer):
    vendors = serializers.SerializerMethodField()

    class Meta:
        model = Retailer
        fields = '__all__'

    def get_vendors(self, value):
        vendors = value.vendors
        return VendorSerializer(vendors, many=True).data
