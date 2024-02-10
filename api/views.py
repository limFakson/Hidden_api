from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Data, FirebaseConfig
from .serializers import DataSerializers, FirebaseConfigSerializers
# Create your views here.

@api_view(['GET'])
def firebaseConfigList(request):
    firebaseConfig = FirebaseConfig.objects.all()
    serializer = FirebaseConfigSerializers(firebaseConfig, many=True)
    
    return Response(serializer.data)
