from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Link
from .serializers import LinkSerializer

# Create your views here.

@api_view (['GET'])
def get_all_nanettework_info(request):
    links = Link.objects.all()
    serializer = LinkSerializer(links, many=True)
    return Response(serializer.data)