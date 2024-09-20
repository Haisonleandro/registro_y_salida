from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.registro.models import registro
from apps.registro.api.serializers import registroserializer

class resgistroApiView(APIView):
    def get(self,request):
        #rests = rest.object.all()
        serializer = registroserializer(registro.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        resgistro.objects.create(nombre=request.data['nombre'],
        categoria=request.data['categoria'], 
        cantidad=request.data['cantidad'],
        fecha=request.data['fecha']),
        serializer = registroserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)