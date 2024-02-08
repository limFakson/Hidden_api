from django.db import models

# Create your models here.
class Data(models.Model):
    organisation_name = CharField(max_lenght=220)
    apiKey = CharField(max_lenght=420)
    projectid = CharField(max_lenght=420)
    appid = CharField(max_lenght=420)