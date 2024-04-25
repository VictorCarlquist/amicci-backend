from django.urls import path
from .views import BriefingViewSet, CategoryViewSet, RetailerViewSet, VendorViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('briefings/', BriefingViewSet.as_view({'get': 'list'})),
    path('briefing/', BriefingViewSet.as_view({'post': 'create'})),
    path('briefing/<int:pk>/', BriefingViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('vendors/', VendorViewSet.as_view({'get': 'list'})),
    path('vendor/', VendorViewSet.as_view({'post': 'create'})),
    path('vendor/<int:pk>/', VendorViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('categories/', CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('category/', CategoryViewSet.as_view({'post': 'create'})),
    path('retailers/', RetailerViewSet.as_view({'get': 'list'})),
    path('retailer/', RetailerViewSet.as_view({'post': 'create'})),
    path('retailer/<int:pk>/', RetailerViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
