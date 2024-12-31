from django.shortcuts import render

from rest_framework import viewsets

from . import serializers, models
# Create your views here.


class ProductViewsets(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer