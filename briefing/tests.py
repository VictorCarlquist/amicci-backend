from django.test import TestCase

from rest_framework import status
from .models import Briefing, Category, Retailer, Vendor
from .views import BriefingViewSet, CategoryViewSet, RetailerViewSet, VendorViewSet

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory


class BriefingEmptyTests(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.base_url = "api/demo"
        return super().setUp()

    def test_briefing_empty_list(self):
        request = self.factory.get(self.base_url + '/briefings/')
        response = BriefingViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, "Não há briefing disponível")


class BriefingTests(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.base_url = "api/demo"

        retailer = Retailer.objects.create(
            name="Retailer 1"
        )

        category = Category.objects.create(
            name="Auto peças",
            description="Produtos automotivos"
        )

        #vendor = Vendor.objects.create(name='Vendor', retailer=retailer)

        self.briefing_data_get = {
            'name': 'Test Briefing',
            'responsible': 'Victor',
            'release_date': '2024-04-25',
            'category': category.name,
            'retailer': retailer.name,
            'availabe':0
        }

        self.briefing_data_update = {
            'name': 'Test Briefing',
            'responsible': 'Victor',
            'release_date': '2024-04-25',
            'category': category.id,
            'retailer': retailer.id,
            'availabe':0
        }

        _briefing_data_default = {
            'name': 'Test Briefing',
            'responsible': 'Victor',
            'release_date': '2024-04-25',
            'category': category,
            'retailer': retailer,
            'availabe':0
        }

        self.briefing = Briefing.objects.create(
            **_briefing_data_default
        )

        return super().setUp()

    def test_briefing_list(self):
        request = self.factory.get(self.base_url + '/briefings/')
        response = BriefingViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_briefing_retrive(self):
        pk = self.briefing.pk
        request = self.factory.get(self.base_url + '/briefing/')
        response = BriefingViewSet.as_view({'get': 'retrieve'})(request, pk=pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("retailer"), self.briefing_data_get.get("retailer"))
        self.assertEqual(response.data.get("category"), self.briefing_data_get.get("category"))

    def test_briefing_update(self):
        pk = self.briefing.pk
        data_to_update = self.briefing_data_update
        data_to_update['name'] = "New value"
        request = self.factory.put(self.base_url + '/briefing/', data=data_to_update)
        response = BriefingViewSet.as_view({'put': 'update'})(request, pk=pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "New value")

    def test_briefing_create(self):
        request = self.factory.post(self.base_url + '/briefing/', data=self.briefing_data_update)
        response = BriefingViewSet.as_view({'post': 'create'})(request)

        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("name"), self.briefing_data_update.get("name"))
