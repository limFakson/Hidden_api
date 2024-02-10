from django.contrib import admin
from .models import Data, FirebaseConfig

# Register your models here.
admin.site.register(Data)
admin.site.register(FirebaseConfig)