from django.shortcuts import render
from .models import Resource
from rest_framework import viewsets
from .serializers import ResourceSerializer

# Create your views here.

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
