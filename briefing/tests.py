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

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("name"), self.briefing_data_update.get("name"))


class VendorsTests(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.base_url = "api/demo"
        return super().setUp()

    def test_vendor_empty_list(self):
        request = self.factory.get(self.base_url + '/vendors/')
        response = VendorViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, "Não há vendor disponível")


class VendorTests(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.base_url = "api/demo"

        self.vendor_data_get = {
            'name': 'Test vendor',
        }

        self.vendor_data_update = {
            'name': 'Test vendor',
        }

        _vendor_data_default = {
            'name': 'Test vendor',
        }

        self.vendor = Vendor.objects.create(
            **_vendor_data_default
        )

        return super().setUp()

    def test_vendor_list(self):
        request = self.factory.get(self.base_url + '/vendors/')
        response = VendorViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_vendor_retrive(self):
        pk = self.vendor.pk
        request = self.factory.get(self.base_url + '/vendor/')
        response = VendorViewSet.as_view({'get': 'retrieve'})(request, pk=pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), self.vendor_data_get.get("name"))

    def test_vendor_update(self):
        pk = self.vendor.pk
        data_to_update = self.vendor_data_update
        data_to_update['name'] = "New value"
        request = self.factory.put(self.base_url + '/vendor/', data=data_to_update)
        response = VendorViewSet.as_view({'put': 'update'})(request, pk=pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "New value")

    def test_vendor_create(self):
        request = self.factory.post(self.base_url + '/vendor/', data=self.vendor_data_update)
        response = VendorViewSet.as_view({'post': 'create'})(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("name"), self.vendor_data_update.get("name"))


class RetailersTests(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.base_url = "api/demo"
        return super().setUp()

    def test_retailer_empty_list(self):
        request = self.factory.get(self.base_url + '/retailers/')
        response = RetailerViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, "Não há retailer disponível")


class RetailerTests(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.base_url = "api/demo"

        self.retailer_data_get = {
            'name': 'Test retailer',
        }

        self.retailer_data_update = {
            'name': 'Test retailer',
        }

        _retailer_data_default = {
            'name': 'Test retailer',
        }

        self.retailer = Retailer.objects.create(
            **_retailer_data_default
        )

        _vendor_data_default = {
            'name': 'Test vendor',
            'retailer': self.retailer
        }

        self.vendor = Vendor.objects.create(
            **_vendor_data_default
        )

        return super().setUp()

    def test_retailer_list(self):
        request = self.factory.get(self.base_url + '/retailers/')
        response = RetailerViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(len(response.data[0].get('vendors')), 1)

    def test_retailer_retrive(self):
        pk = self.retailer.pk
        request = self.factory.get(self.base_url + '/retailer/')
        response = RetailerViewSet.as_view({'get': 'retrieve'})(request, pk=pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), self.retailer_data_get.get("name"))
        self.assertEqual(len(response.data.get('vendors')), 1)


    def test_retailer_update(self):
        pk = self.retailer.pk
        data_to_update = self.retailer_data_update
        data_to_update['name'] = "New value"
        request = self.factory.put(self.base_url + '/retailer/', data=data_to_update)
        response = RetailerViewSet.as_view({'put': 'update'})(request, pk=pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "New value")

    def test_retailer_create(self):
        request = self.factory.post(self.base_url + '/retailer/', data=self.retailer_data_update)
        response = RetailerViewSet.as_view({'post': 'create'})(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("name"), self.retailer_data_update.get("name"))