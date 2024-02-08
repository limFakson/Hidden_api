from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Data
from .serializers import DataSerializers
# Create your views here.

api_view([GET])
def dataList(request):
    data = Data.objects.all()
    serializer = DataSerializers(tasks, many-True)
    
    return Response(serializer.data)
