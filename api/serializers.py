from rest_framework import serializers
from .models import Data, FirebaseConfig

class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class FirebaseConfigSerializers(serializers.ModelSerializer):
    data = DataSerializers()

    class Meta:
        model = FirebaseConfig
        fields = ['data', 'id']  # Include other fields if necessary