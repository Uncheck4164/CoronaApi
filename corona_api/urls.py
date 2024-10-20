from django.urls import path, include
from rest_framework import routers
from .api import CoronaViewSet
from .views import get_products_data

router = routers.DefaultRouter()
router.register('api/corona', CoronaViewSet, 'corona')
urlpatterns = [
    path('', include(router.urls)),
    path('api/corona/products', get_products_data, name='get_products_data'),
]