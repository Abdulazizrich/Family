from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from mainApp.views import *

router = DefaultRouter()

router.register('suv',SuvViewSet)
router.register('mijoz',MijozViewSet)
router.register('haydovchi',HaydovchiViewSet)
router.register('admin',AdminViewSet)
router.register('buyurtma',BuyurtmaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
