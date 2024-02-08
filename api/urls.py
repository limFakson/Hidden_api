from django.urls import path
from .views import dataList

urlpatterns = [
    path('', dataList, name=dataList)
]
