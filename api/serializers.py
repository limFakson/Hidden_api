from rest_framework import serializers

from .models import Data

class DataSerializers(serializers.MOdelSerializers):
    class Meta:
        model = Data
        fields = '__all__'