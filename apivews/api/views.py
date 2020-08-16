from rest_framework.viewsets import ModelViewSet
from ..models import Temp
from .serializers import TempSerializer


# to access the data before saving use request not serializer

class TempView(ModelViewSet):
    queryset = Temp.objects.all()
    serializer_class = TempSerializer

    def perform_create(self, serializer):
        print(self.request.data['temp_field'])
        return super().perform_create(serializer)
