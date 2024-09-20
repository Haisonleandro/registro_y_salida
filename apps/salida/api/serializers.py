from rest_framework.serializers import ModelSerializer
from apps.salida.models import salida

class salidaserializer(ModelSerializer):
    class Meta:
        model = salida
        fields = ['nombre','categoria','cantidad','fecha_salida']