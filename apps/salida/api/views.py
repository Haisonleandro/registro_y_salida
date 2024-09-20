from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.salida.models import salida
from apps.salida.api.serializers import salidaserializer

class salidaApiView(APIView):
    def get(self,request):
        #rests = rest.object.all()
        serializer = salidaserializer(salida.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        salida.objects.create(nombre=request.data['nombre'],
        categoria=request.data['categoria'], 
        cantidad=request.data['cantidad'],
        fecha_salida=request.data['fecha']),
        serializer = salidaserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)