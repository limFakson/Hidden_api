from django.urls import path
from . import views

urlpatterns = [
    path('', views.firebaseConfigList, name="firebase-Config")
]
