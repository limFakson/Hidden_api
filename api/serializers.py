from rest_framework import serializers
from .models import Data, FirebaseConfig

class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('apiKey', 
                  'projectid', 
                  'appid', 
                  'authDomain', 
                  'storageBucket', 
                  'messagingSenderId', 
                  'measurementId'
                  )


class FirebaseConfigSerializers(serializers.ModelSerializer):
    data = DataSerializers()

    class Meta:
        model = FirebaseConfig
        fields = ['data']  # Exclude 'id' by not including it in the list