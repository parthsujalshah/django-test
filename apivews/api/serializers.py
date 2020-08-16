from rest_framework.serializers import ModelSerializer
from ..models import Temp


class TempSerializer(ModelSerializer):
    class Meta:
        model = Temp
        fields = ['id', 'temp_field']