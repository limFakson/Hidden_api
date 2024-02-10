from django.db import models

# Create your models here.
class Data(models.Model):
    apiKey = models.CharField(max_length=420)
    projectid = models.CharField(max_length=420)
    appid = models.CharField(max_length=420)
    authDomain = models.CharField(max_length=420)
    storageBucket = models.CharField(max_length=420)
    messagingSenderId = models.CharField(max_length=420)
    measurementId = models.CharField(max_length=420)


class FirebaseConfig(models.Model):
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
