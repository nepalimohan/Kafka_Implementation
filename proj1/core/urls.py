from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from product import views

router = DefaultRouter()
router.register(r'products', views.ProductViewsets, basename='products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
