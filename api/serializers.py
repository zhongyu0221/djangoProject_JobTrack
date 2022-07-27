from rest_framework import serializers
from learnDRF.models import Item



@api_view(['GET'])
class Itemserializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'