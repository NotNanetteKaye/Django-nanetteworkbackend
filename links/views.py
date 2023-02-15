from django.shortcuts import render
from rest_framework.decorators import api_view
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


@api_view(['GET', 'POST', 'DELETE'])
def nanettework_details(request):
    if request.method == 'POST':
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET': 
    else:
        

