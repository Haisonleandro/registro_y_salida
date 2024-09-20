from rest_framework.serializers import ModelSerializer
from apps.registro.models import registro

class registroserializer(ModelSerializer):
    class Meta:
        model = registro
        fields = ['nombre','categoria','cantidad','fecha']